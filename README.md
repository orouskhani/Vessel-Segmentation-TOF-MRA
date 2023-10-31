# Vessel-Segmentation-TOF-MRA
In this project, we have devised a technique employing conventional segmentation algorithms for the automatic segmentation of brain vessels within 3D TOF MRA images. Despite the absence of vessel labels in the TOF-MRA dataset, we employed established methods such as Hessian Vessel enhancement, OTSU, and the maximum connection approach to effectively eliminate noise and false positives. Ultimately, we are able to determine the precise location of the vessels, which can then be utilized in various applications. As an example, in the research paper titled "nnU-Net Deep Learning with Vessel Information for Intracranial Aneurysm Segmentation on 3D TOF-MRA," we demonstrate how we automatically crop the TOF-MRA images using the extracted vessel location information.

![image](https://github.com/orouskhani/Vessel-Segmentation-TOF-MRA/blob/main/Model.jpg)


![image](https://github.com/orouskhani/Vessel-Segmentation-TOF-MRA/blob/main/result.png)

