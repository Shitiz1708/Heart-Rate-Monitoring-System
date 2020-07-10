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
    
    def extract_features(video_path):
        frame = self.frame_ROI/255.0
        frame = np.array(frame,dtype='float16')
        frame[:,:,0] = 0
        frame[:,:,2] = 0
        ROI_1 =frame[:int(frame.shape[0]*0.15),:,:]
        X_video_1.append(ROI_1)
        count+=1
    
    def calculate_bpm(self):
        self.bpm = 20


    def run(self):
        frame,aligned_frame = self.fd.detect_face(self.frame_in)
        self.frame_out = frame
        self.frame_ROI = aligned_frame
        self.calculate_bpm()