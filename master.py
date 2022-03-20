import cv2
import numpy as np
from CameraCalibration import *
from main import *
import pickle

objfile = open('objpoints.pkl', 'rb')
objpoints = pickle.load(objfile)
objfile.close()

imgfile = open('imgpoints.pkl', 'rb')
imgpoints = pickle.load(imgfile)
imgfile.close()

#Calibrate image before measurement
Calibrate(objpoints, imgpoints, (2122, 3226), 'images/blue_scan_300.jpg')

measurement('images/proper_env.png')

