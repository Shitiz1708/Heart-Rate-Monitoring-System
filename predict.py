import numpy as np
import cv2
import os

class Predict(object):
    def __init__(self):
        self.frame_in = np.zeros((480,640,3),dtype=np.uint8)
        self.frame_out = np.zeros((480,640,3),dtype=np.uint8)
        self.fd = Face_Detector()
    def 