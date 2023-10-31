# PART 1: Vessel segmentation to aneurysm segmentation
In this project, we have devised a technique employing conventional segmentation algorithms for the automatic segmentation of brain vessels within 3D TOF MRA images. Despite the absence of vessel labels in the TOF-MRA dataset, we employed established methods such as Hessian Vessel enhancement, OTSU, and the maximum connection approach to effectively eliminate noise and false positives. Ultimately, we are able to determine the precise location of the vessels, which can then be utilized in various applications. As an example, in the research paper titled "nnU-Net Deep Learning with Vessel Information for Intracranial Aneurysm Segmentation on 3D TOF-MRA," we demonstrate how we automatically crop the TOF-MRA images using the extracted vessel location information.

![image](https://github.com/orouskhani/Vessel-Segmentation-TOF-MRA/blob/main/Model.jpg)


![image](https://github.com/orouskhani/Vessel-Segmentation-TOF-MRA/blob/main/result.png)

# PART 2: Aneurysm segmentation with multimodality imaging
In part 2 of this project, we used two modalities to train the model. </br> 
1- The original image
2- Attention image: Original image * Vessel image

Note: The vessel image is derived from Hessian. Then, it normalized to [0,1]

original image--> [0,255]
vessel image --> [0,1]
So  original image * vessel image --> Normalized between 0,255

**Result--> ** While training the model with the original images achieved Dice coefficient equals 0.48, multimodality training of the original dataset and data derived from enhanced hessian provides the Dice close to 0.57.  
