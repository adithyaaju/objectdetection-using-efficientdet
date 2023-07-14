from Detector import *


modelURL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d4_coco17_tpu-32.tar.gz"

classFile = "coco.names"
imagePath = "test2.jpeg"
videoPath = "1410202020543050_20201014205430.mp4"
threshold = 0.5

detector = Detector()
detector.readClasses(classFile)
detector.downloadModel(modelURL)
detector.loadModel()
#detector.predictImage(imagePath, threshold)
detector.predictVideo(videoPath, threshold)