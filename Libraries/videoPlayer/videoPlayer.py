import tkinter as tk  # for Python3

import threading
from time import perf_counter, sleep
import imageio
from PIL import Image, ImageTk

class videoPlayer():
    def __init__(self, label, hz):
        self.hz = hz
        self.video1 = "././Assets/Videos/BailPlateDown.mp4"
        self.video2 = "././Assets/Videos/video2.mp4"
        self.label = label
        self.videoChange=False
        self.videoNumber=1

    def playVideo(self):
        self.player.play()

    def changeVideo(self, videoNumber):
        self.videoNumber=videoNumber
        self.videoChange=True

    def load(self, label, hz):
        video1_frame_data = imageio.get_reader(self.video1)
        video2_frame_data = imageio.get_reader(self.video2)

        if hz > 0:
            frame_duration = float(1 / hz)
        else:
            frame_duration = float(0)
        
        while True:
            before = perf_counter()
            if self.videoNumber==1:
                frame_data = video1_frame_data
            elif self.videoNumber==2:
                frame_data = video2_frame_data

            for image in frame_data.iter_data():
                if self.videoChange==True:
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

            if self.videoChange==True:
                self.videoChange=False

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load, args=(self.label, self.hz))
        thread.daemon = 1
        thread.start()