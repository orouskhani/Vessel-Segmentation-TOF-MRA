# Vessel-Segmentation-TOF-MRA
In this project, we develop a method using traditional segmentation algorithms to segment the brain vessels in 3D TOF MRA automatically. While we have no labels for vessels in the TOF-MRA dataset, we used traditional methods including Hessian Vessel enhancement and OTSU along with the maximum connection method to remove noise and false positives. Finally, we can calculate the location of vessels and it can be used in other tasks such as segmenting an aneurysm. We can crop the original image regarding the vessel's location provided by our method. 



