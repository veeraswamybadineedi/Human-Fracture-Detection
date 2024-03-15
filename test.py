from IPython import display
import ultralytics
from ultralytics import YOLO
import pickle
from IPython.display import display, Image
import os, random
import cv2


from roboflow import Roboflow
# rf = Roboflow(api_key="ANrDtEusrBTk630VFcI8")
# project = rf.workspace("fracturedetection-qohz3").project("human-bone-fracture-detection")
# dataset = project.version(1).download("yolov8")

filename="veera.pkl"
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

#Save the image
# result = loaded_model.predict("download.jpg", confidence=40, overlap=30)
# cv2.imwrite("x1.jpg",result)
loaded_model.predict("a.jpg", confidence=40, overlap=30).save('prediction3.jpg')