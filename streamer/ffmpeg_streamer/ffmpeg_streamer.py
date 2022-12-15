# liberaries
import subprocess
import pathlib
import numpy as np

# project dependencies
from streamer.streamer import StreamerInterface

class FFmpegStreamer(StreamerInterface):
    def __init__(self,buffer:pathlib.Path):
        self.started = False
        self.buffer = pathlib.Path(buffer)
        # insure that buffering directory exists
        self.buffer.mkdir(parents=True, exist_ok=True)

    
    def setSize(self, size: tuple):
        self.size = size
        
    def write(self, frame:np.ndarray):
        if self.started:
            self.ffmpeg.stdin.write(frame)
            return True
        else:
            return False


    def startStreaming(self):
        ffmpeg = pathlib.Path(__file__).parent / 'ffmpeg_command.sh'
        command = ['bash',ffmpeg, f"{self.buffer.absolute()}/live.m3u8",f'{self.size[0]}x{self.size[1]}']
        self.ffmpeg = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        self.started = True

    def __del__(self):
        if self.ffmpeg != None:
            self.ffmpeg.kill()
    
    
   