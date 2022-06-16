import os, numpy as np, nibabel as nib
from os.path import join, basename
from tqdm import tqdm
from glob import glob, iglob
from bidsio import BIDSLoader
from settings import eval_settings


def chk_CRC(src_dir:str, fname:str='*', recursive:bool=True):
    for path in tqdm(sorted(list(iglob(f'{src_dir}/{fname}', recursive={recursive}))), desc='CRC Checking'):
        try:
            _ = nib.load(path).get_fdata()
        except Exception as e:
            tqdm.write(path+': '+e.__str__())

def convert_to_BIDS(src_dir:str, dst_dir:str, fname:str='*.nii.gz', recursive:bool=True):
    for path in tqdm(sorted(list(iglob(join(src_dir, fname), recursive=recursive))), desc='Convert to BIDS', colour='green', dynamic_ncols=True):
        # Directory configuration
        first_dir = 'sub-r'+basename(path)[3:6]+'s'+basename(path)[7:10]
        target_dir = join(dst_dir, first_dir, 'ses-1', 'anat')
        os.makedirs(target_dir, exist_ok=True)
        fname = join(f'{first_dir}_{"ses-1"}_{"space-MNI152NLin2009aSym_label_L_desc-T1lesion_mask.nii.gz"}')

        # Save as NiBabel file        
        nib.load(path).to_filename(join(target_dir, fname))


path = os.getcwd() + '/output_Task505_ATLAS_OriginTest' #Check 1

file_list = os.listdir(path)
file_list_nii = [file for file in file_list if file.endswith(".nii.gz")]

for i in range(len(file_list_nii)):
    img_path = path+"/"+file_list_nii[i]
    img = nib.load(img_path) #nifti 파일에서 이미지 영역만 가져오기

    fname = file_list_nii[i].split(".")
          
    directory1 = "sub-r"+fname[0][3:6]+"s"+fname[0][7:]
    directory2 = "ses-1"
    directory3 = "anat"
                
    path2 = os.getcwd() + '/final_labels/' #Check2
    final_directory = path2+directory1+"/"+directory2+"/"+directory3+"/"
                
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
               
    #fname = os.path.basename(file_list_nii1[i])
    refname = directory1+"_"+directory2+"_space-MNI152NLin2009aSym_label_L_desc-T1lesion_mask.nii.gz"
    img.to_filename(os.path.join(final_directory,'{}'.format(refname)))  # Save as NiBabel file

if __name__ == '__main__':
    # chk_CRC('output_Task507_ATLAS_ATLAS_3d_fullres_1000ep_10_0', fname='*.nii.gz')
    # union()
    convert_to_BIDS(model_prediction_dir, BIDS_formatted_dir)
    BIDSLoader.write_dataset_description(BIDS_formatted_dir, eval_settings['PredictionBIDSDerivativeName'][0])
    os.system(f'cd {BIDS_formatted_dir} && zip -qr ../{zip_filename} *')