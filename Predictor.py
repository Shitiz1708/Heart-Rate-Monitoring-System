import numpy as np
import cv2
import os
from Face_Detector import Face_Detector

class Predictor(object):
    def __init__(self):
        self.frame_in = np.zeros((480,640,3),dtype=np.uint8)
        self.frame_out = np.zeros((480,640,3),dtype=np.uint8)
        self.frame_ROI = np.zeros((480,640,3),dtype=np.uint8)
        self.bpm = 0
        self.fd = Face_Detector()
    
    def calculate_bpm(self,frame):
        self.bpm = 20


    def run(self):
        frame,aligned_frame = self.fd.detect_face(self.frame_in)
        