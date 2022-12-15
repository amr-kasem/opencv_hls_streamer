from streamer.streamer import StreamerInterface
from camera.camera import CameraInterface
class CameraHandler:
    def __init__(self, camera:CameraInterface, streamer:StreamerInterface):
        self.camera = camera
        self.streamer = streamer
        self.camera.connect()
        self.streamer.setSize(self.camera.getSize())
        self.streamer.startStreaming()
        
    def run(self):
        while self.camera.isAvailable():
            frame = self.camera.getFrame()
            if not self.streamer.write(frame):
                print('failed to write a frame')
