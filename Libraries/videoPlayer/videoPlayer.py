import tkinter as tk  # for Python3
from tkvideo import tkvideo

import threading
from time import perf_counter, sleep
import imageio
from PIL import Image, ImageTk

videoOnPlay=1

class videoPlayer():
    def __init__(self, label, hz):
        self.hz = hz
        self.path = "././Assets/Videos/BailPlateDown.mp4"
        self.label = label
        self.player = tkvideo(self.path, self.label, loop = 1)

    def playVideo(self):
        self.player.play()

    def changeVideo(self):
        videoOnPlay=0
        self.path = "././Assets/Videos/video2.mp4"
        self.play()

    def load(self, path, label, hz):
        frame_data = imageio.get_reader(path)

        if hz > 0:
            frame_duration = float(1 / hz)
        else:
            frame_duration = float(0)
        
        videoOnPlay=1
        while True:
            before = perf_counter()
            for image in frame_data.iter_data():
                if videoOnPlay==0:
                    break
                frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                label.config(image=frame_image)
                label.image = frame_image

                diff = frame_duration + before
                after = perf_counter()
                diff = diff - after 
                if diff > 0:
                    sleep(diff)
                before = perf_counter()
                videoOnPlay

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load, args=(self.path, self.label, self.hz))
        thread.daemon = 1
        thread.start()