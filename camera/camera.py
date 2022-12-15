class CameraInterface():
    def __init__(self, source:str):
        raise NotImplementedError
    def connect(self):
        raise NotImplementedError
    def disconnect(self):
        raise NotImplementedError
    def getSize(self):
        raise NotImplementedError
    def getFPS(self):
        raise NotImplementedError
    def getFrame(self):
        raise NotImplementedError
    def isAvailable(self):
        raise NotImplementedError
