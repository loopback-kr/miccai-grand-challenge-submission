import os
import nibabel as nib
import numpy as np

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