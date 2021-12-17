import tkinter as tk  # for Python3

import threading
from time import perf_counter, sleep
import imageio
from PIL import Image, ImageTk

class videoPlayer():
    def __init__(self, label):
        self.label = label
        self.photo1 = tk.PhotoImage(file="Assets/Videos/11.png")
        self.photo2 = tk.PhotoImage(file="Assets/Videos/22.png")
        self.photo3 = tk.PhotoImage(file="Assets/Videos/33.png")
        self.photo4 = tk.PhotoImage(file="Assets/Videos/44.png")
        self.frames = [self.photo1, self.photo2, self.photo3, self.photo4]

    def load(self):
        while True:
            for i in range(4):
                self.label.config(image=self.frames[i])
                self.label.image = self.frames[i]
                sleep(1)

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load)
        thread.daemon = 1
        thread.start()