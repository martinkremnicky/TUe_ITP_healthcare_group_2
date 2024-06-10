import nibabel as nib

def read_nifti(filepath):
    """
    Read a NIfTI file and return the image data as a PyTorch tensor.
    Args:
        filepath (str): Path to the NIfTI file.
    Returns:
        
    """
    # Load NIfTI file
    img = nib.load(filepath)
    # Get the image data as a NumPy array
    img_data = img.get_fdata()
    # Convert the NumPy array to a PyTorch tensor
    # img_tensor = torch.from_numpy(img_data)
    return img_data
