#!/usr/bin/env python3
class StreamerInterface:
    def __init__(_self, bufferDirectory):
        raise NotImplementedError
    def startStreaming(self):
        raise NotImplementedError
    def write(self, frame):
        raise NotImplementedError
    def onStarted(_self):
        raise NotImplementedError
    def onError(_self):
        raise NotImplementedError
    def onProgress(_self):
        raise NotImplementedError
    def onCopleneted(_self):
        raise NotImplementedError
    def setSize(_self, size:tuple):
        raise NotImplementedError