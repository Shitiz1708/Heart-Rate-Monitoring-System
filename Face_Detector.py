import numpy as np
import cv2
import os
from mtcnn.mtcnn import MTCNN
from FaceAligner import FaceAligner

class Face_Detector(object):
    def __init__(self):
        self.fa = FaceAligner()
        self.detector = MTCNN()
    
    def detect_face(self,frame):
        faces = self.detector.detect_faces(frame)
        aligned_frame = self.fa.align(frame,faces)
        cv2.rectangle(frame,(shape[54][0], shape[29][1]), #draw rectangle on right and left cheeks
                        (shape[12][0],shape[33][1]), (0,255,0), 0)


