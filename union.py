import os, numpy as np, nibabel as nib, SimpleITK as sitk, json, csv, re, random, tqdm
from tqdm.contrib import tzip
from os.path import join, basename, exists, splitext
from glob import glob, iglob

A_PATH = os.getenv('A_PATH', default=None)
B_PATH = os.getenv('B_PATH', default=None)
DST_PATH = os.getenv('DST_PATH', default=None)

a_paths = sorted(glob(join(A_PATH, '*.nii.gz')))
b_paths = sorted(glob(join(B_PATH, '*.nii.gz')))
os.makedirs(DST_PATH, exist_ok=True)

for a_path, b_path in tzip(a_paths, b_paths, dynamic_ncols=True):
    if basename(a_path) != basename(b_path):
        tqdm.write(f'Not matched: {basename(a_path)}, {basename(b_path)}')
    else:
        a = sitk.ReadImage(a_path)
        b = sitk.ReadImage(b_path)

        a_img = sitk.GetArrayFromImage(a)
        b_img = sitk.GetArrayFromImage(b)

        union_img = np.logical_or(a_img, b_img).astype(np.uint8)

        union = sitk.GetImageFromArray(union_img)
        union.CopyInformation(a)
        sitk.WriteImage(union, join(DST_PATH, basename(a_path)))