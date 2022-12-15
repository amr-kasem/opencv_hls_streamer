# liberaries
import numpy as np
import sys

# project dependencies
from streamer.streamer import StreamerInterface

class StdoutStreamer(StreamerInterface):
    def __init__(self,buffer, size:tuple):
        pass
    def write(self,frame:np.ndarray):
        sys.stdout.buffer.write(frame.tobytes())