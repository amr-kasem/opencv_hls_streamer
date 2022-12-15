class RunnerInterface:
    def __init__(self):
        raise NotImplementedError
    def start(self):
        raise NotImplementedError
    def initRoutines(self, routines:list):
        raise NotImplementedError