# Camera_intrinsic_calibration
---
This repository contains multi-camera intrinsic calibration using opencv.

---
## Instruction:
In order to generate the distortion and calibration parametrs, execute 'cam_cal_dist_mtx_generator.py'.
Once 'mtx' and 'dist' parameters are saved, use 'cam_intrinsic_cal.py' to undistort the input images. If not specifying an output folder, the undistorted images will be overwritten on the input images. 
To replace the inputs images with undistorted ones, keep the input and output parent directories the same.

