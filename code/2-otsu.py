import numpy as np
import nibabel as nib
from skimage.filters import threshold_otsu
from scipy import ndimage


# load the 3D NIfTI file
nii_file = nib.load('41.nii.gz')
data = nii_file.get_fdata()

# apply Otsu's thresholding to the data
threshold = threshold_otsu(data)
binary = (data > threshold).astype(int)

# save the binary segmentation as a new NIfTI file
nii_binary = nib.Nifti1Image(binary, nii_file.affine, header=nii_file.header)
nib.save(nii_binary, '412.nii.gz')
