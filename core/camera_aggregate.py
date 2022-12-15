from core.camera_handler import CameraHandler
from runner.runner import RunnerInterface

class CameraAggregate:
    def __init__(self,runner:RunnerInterface , cameras:list[CameraHandler]):
        self.runner = runner
        self.cameras = cameras

    def run(self):
        routines = [cam.run for cam in self.cameras]
        self.runner.initRoutines(routines)
        self.runner.start()
