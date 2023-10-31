import numpy as np
import nibabel as nib
from skimage.measure import regionprops_table
from cc3d import connected_components

# Load the NIfTI file
nifti = nib.load('412.nii.gz')
data = nifti.get_fdata()

# Threshold the data to get a binary segmentation
threshold = 0.5  # set the threshold
binary_data = data > threshold

# Label connected regions
labeled_data = connected_components(binary_data)

# Get the region properties
props = regionprops_table(labeled_data, properties=('label', 'area'))

# Find the n largest regions
n_regions = 3  # set the number of regions you want to select
largest_regions = np.argsort(props['area'])[-n_regions:][::-1]

# Create a mask for each selected region
selected_regions_mask = np.zeros_like(labeled_data, dtype=bool)
for region_label in largest_regions:
    selected_regions_mask |= labeled_data == props['label'][region_label]

# Save the segmented data as a NIfTI file
seg_nifti = nib.Nifti1Image(selected_regions_mask.astype(np.uint8), nifti.affine, nifti.header)
nib.save(seg_nifti, '413.nii.gz')
