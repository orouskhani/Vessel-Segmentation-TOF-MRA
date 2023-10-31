import nibabel as nib
import numpy as np
import itk


# **********************************************************************
# Load the NIfTI image data from the last part: 3-connected component.py
img = nib.load('413.nii.gz')
# Load the 3D Nifti file try to crop
input_image = itk.imread('adam_0041.nii.gz')
#***********************************************************************

data = img.get_fdata()
# Create a binary mask of the non-zero values
mask = (data != 0)

# Find the minimum and maximum x, y, and z indices of the non-zero values
nz_indices = np.argwhere(mask)
min_x, min_y, min_z = np.min(nz_indices, axis=0)
max_x, max_y, max_z = np.max(nz_indices, axis=0)

print("Minimum x index: ", min_x)
print("Maximum x index: ", max_x)
print("Minimum y index: ", min_y)
print("Maximum y index: ", max_y)
print("Minimum z index: ", min_z)
print("Maximum z index: ", max_z)

# Define the bounding box
point1 = [min_x, min_y, min_z]
point2 = [max_x, max_y, max_z]
min_point = [min(point1[i], point2[i]) for i in range(3)]
max_point = [max(point1[i], point2[i]) for i in range(3)]
size = [max_point[i] - min_point[i] + 1 for i in range(3)]
index = min_point

# Define the crop region
crop_region = itk.ImageRegion[3]()
crop_region.SetSize(size)
crop_region.SetIndex(index)

# Create a region of interest filter object
roi_filter = itk.RegionOfInterestImageFilter.New(input_image)
roi_filter.SetRegionOfInterest(crop_region)

# Apply the filter to the input image
cropped_image = roi_filter.GetOutput()
cropped_image.Update()

# Save the cropped image as a new Nifti file
itk.imwrite(cropped_image, 'file.nii.gz')
