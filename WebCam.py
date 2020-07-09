import cv2
import os

class WebCam(object):
    def __init__(self):
        self.cap = None

    def start(self):
        print('Starting Webcam')
        self.cap = cv2.VideoCapture(0)
        self.valid = False
        try:
            res = self.cap.read()
            self.shape = res[1].shape
            print(self.shape)
            self.valid = True
        except:
            self.shape = None
    
    def getFrame(self):
        if(self.valid):
            ret,frame = self.cap.read()
            frame = cv2.flip(frame,1)
        else:
            frame = np.ones((480,640,3),dtype=np.uint8)
            col = (0,256,256)
            cv2.putText(frame, "(Error: Camera not accessible)",
                       (65,220), cv2.FONT_HERSHEY_PLAIN, 2, col)
        return frame
    
    def stop(self):
        if self.cap is not None:
            self.cap.release()
            print("[INFO] Stop webcam")
