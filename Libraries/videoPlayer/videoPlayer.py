import tkinter as tk  # for Python3

import threading
from time import perf_counter, sleep
import imageio
from PIL import Image, ImageTk

class videoPlayer():
    def __init__(self, label):
        self.label = label

    def load(self):
        while True:
            for i in range(15):
                fileLocation = "Assets/Frames/Upper-plate-down/" + str(i) + ".png"
                self.frame = tk.PhotoImage(file=fileLocation)
                self.label.config(image=self.frame)
                self.label.image = self.frame
                sleep(0.3)

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load)
        thread.daemon = 1
        thread.start()