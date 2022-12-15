# liberaries
import cv2

# project dependencies
from camera.camera import CameraInterface

class CVCamera(CameraInterface):
    def __init__(self, source:str):
        self.source = source
    def __del__(self):
        self.disconnect()
    def connect(self):
        self._videoCapture = cv2.VideoCapture(self.source) 
        return self.isAvailable()
    def disconnect(self):
        self._videoCapture.release()
    def isAvailable(self):
        return self._videoCapture.isOpened()
    
    def getSize(self):
        if(self.isAvailable()):
            return (int(self._videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(self._videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        else:
            raise IOError('camera in not connected')
    
    def getFPS(self):
        if(self.isAvailable()):
            return self._videoCapture.get(cv2.CAP_PROP_FPS)
        else:
            raise IOError('camera in not connected')
    
    def getFrame(self):
        if(self.isAvailable()):
            ret,frame =  self._videoCapture.read()
            cv2.waitKey(1)
            if(ret):
                return frame
        raise IOError('camera in not connected')
