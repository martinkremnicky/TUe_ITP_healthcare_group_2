import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.ndimage as ndi

directory = 'C:\Users\hilde\Documents\Technische Universiteit Eindhoven\Int. Team Project\TUe_ITP_healthcare_group_2\data_augmentation\image_files'
#output_folder = '/Users/christosmichalopoulos/Desktop/5ARIP_Images_R'
loaded_items = []

# Iterate over all folders in the directory
for folder_name in sorted(os.listdir(directory)):
    folder_path = os.path.join(directory, folder_name)
    # Check if the current item is a folder
    if os.path.isdir(folder_path):        
        print("Folder:", folder_name)

        # Iterate over all files in the folder
        for item_name in sorted(os.listdir(folder_path)):
            item_path = os.path.join(folder_path, item_name)
            
            # Check if the current item is a file
            if os.path.isfile(item_path) and 'ROI' in item_name and item_name != '.DS_Store':
                print("File:", item_name)
                print('\n')
                items = nib.load(item_path)
                loaded_items.append(items) 
            
for data_item in loaded_items:
        data = data_item.get_fdata()

        rotated_data = ndi.rotate(data, 90)

        split_data1 = rotated_data[:, :rotated_data.shape[1] // 2, :]
        split_data2 = rotated_data[:, rotated_data.shape[1] // 2:, :]

        split_img1 = nib.Nifti1Image(split_data1, affine=data_item.affine)
        split_img2 = nib.Nifti1Image(split_data2, affine=data_item.affine)

        output_file_path1 = os.path.join(output_folder, 'left_' + os.path.basename(data_item.get_filename()))
        output_file_path2 = os.path.join(output_folder, 'right_' + os.path.basename(data_item.get_filename()))
        nib.save(split_img1, output_file_path1)
        nib.save(split_img2, output_file_path2)

        if 'left' in data_item.get_filename():
                flipped_data = np.flip(split_img1, axis=1)
                flipped_img = nib.Nifti1Image(flipped_data, affine=data_item.affine)
                output_file_path = os.path.join(output_folder, 'flipped_' + os.path.basename(data_item.get_filename()))
                nib.save(flipped_img, output_file_path)
