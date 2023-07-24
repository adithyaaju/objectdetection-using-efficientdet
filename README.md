# Objectdetection-using-efficientdet
## Abstract :

In my efficientdet project the code implements a class called "Detector" that performs object detection using a pre-trained model, TensorFlow, and OpenCV. It relies on several files and resources to carry out the task effectively.At the core of the code is a pre-trained model that is obtained by downloading it from a specified URL. The model file, in a saved model format, contains the trained weights and architecture necessary for object detection. The downloaded model is extracted into a cache directory for subsequent use.In addition to the model, the code requires a file containing class labels. This file, specified by classesFilePath, includes a list of class labels or categories that the object detection model can recognize. The code reads this file and stores the class labels in a list, enabling the mapping of predicted class indices to their respective labels.
                                                   The code accepts input images and videos for object detection. When using the predictImage method, an image file is provided as input. The code reads the image file using OpenCV and applies object detection using the pre-trained model. Bounding boxes are drawn around the detected objects, and class labels with corresponding confidence scores are displayed. The resulting image, including the bounding boxes and labels, is saved as a new image file with the same name as the pre-trained model, but with the extension ".jpg". The image is also displayed for visual inspection.For video processing, the predictVideo method takes a video file as input. The code uses OpenCV to read the video frame by frame. Object detection is performed on each frame using the pre-trained model, and bounding boxes with class labels are drawn around the detected objects. The resulting video, including the bounding boxes and labels, is saved as "output_video.mp4" in MP4 format. Additionally, the code calculates the frames per second (FPS) and inference time for each frame, and overlays this information on the video. The processed video is displayed in real-time for visual monitoring.
Overall, this code combines TensorFlow, OpenCV, a pre-trained model, class label files, and input images or videos to perform object detection and generate visual outputs with bounding boxes and class labels.

## System Confugration 

- System OS : Ubuntu 20.04
- Memory : 15.5 GiB
- Disk space : 480.1 GB
- Processor : Intel® Core™ i5-7300U CPU @ 2.60GHz × 4
- Graphics : Mesa Intel® HD Graphics 620 (KBL GT2)
- IDE : Pycharm

## Packages And Libraries Required 

- numpy
- os
- imutils
- Cv2
- tensorflow
- keras

## FPS and Inference Time examined in Efficientdet

----------------------------------------------------
|SI no|Resolution         |Inference Time  |FPS     |
|-----|-------------------|----------------|--------|
|1    |640x480            |2862.0 ms       |0.35    |
|2    |1280x720           |2739.0 ms       |0.37    |
|3    |1920x1080          |7956.0 ms       |0.36    |
|4    |2560x1440          |8028.0 ms       |0.35    |
|5    |2048x1080          |7872.0 ms       |0.34    |
|6    |3840x2160          |7971.0 ms       |0.37    |
|7    |7680x4320          |2880.0 ms       |0.35    |
