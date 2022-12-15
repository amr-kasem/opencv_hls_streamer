# libraries
from threading import Thread

# project deependencies
from runner.runner import RunnerInterface

class ThreadingRunner(RunnerInterface):
    def __init__(self):
        pass
    def __del__(self):
        for t in self.threads:
            t.join()
    def initRoutines(self, routines:list):
        self.threads = [Thread(target=r) for r in routines]
        
        
    def _run(self):
        for t in self.threads:
            t.start()
        
    def start(self):
        self._run()
