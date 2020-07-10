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
        box = faces[0]['box']
        aligned_frame = self.fa.align(frame,faces)
        cv2.rectangle(frame,(box[0], box[1]), #draw rectangle on right and left cheeks
                        (box[0]+box[2],box[1]+box[3]), (0,255,0), 3)
        return frame,aligned_frame


