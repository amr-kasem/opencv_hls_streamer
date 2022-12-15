from streamer.ffmpeg_streamer.ffmpeg_streamer import FFmpegStreamer
from camera.opencv_camera.opencv_camera import CVCamera
from core.camera_handler import CameraHandler
from runner.threading_runner.threading_runner import ThreadingRunner
from core.camera_aggregate import CameraAggregate


def getCameraHandler(videoSrc, bufferDir):
    camera = CVCamera(videoSrc)
    streamer = FFmpegStreamer(bufferDir)
    handler = CameraHandler(camera=camera,streamer=streamer)
    return handler    


if __name__ == "__main__":
    handler0 = getCameraHandler('/dev/video0','/dev/shm/hls0')
    runner = ThreadingRunner()
    cameraAggregator = CameraAggregate(
        runner,
        [
            handler0,
        ]
    )
    cameraAggregator.run()
    
