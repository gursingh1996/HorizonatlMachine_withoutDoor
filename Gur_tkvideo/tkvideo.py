import tkinter as tk  # for Python3
import threading
import imageio
from PIL import Image, ImageTk

videoOnPlay=1

class tkvideo():
    def __init__(self, path, label):
        self.path = path
        self.label = label
    
    def load(self, path, label):
        frame_data = imageio.get_reader(path)
        while videoOnPlay:
            for image in frame_data.iter_data():
                if not videoOnPlay: 
                    break
                frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                label.config(image=frame_image)
                label.image = frame_image

    def playVideo(self):
        global videoOnPlay
        videoOnPlay=1
        thread = threading.Thread(target=self.load, args=(self.path, self.label))
        thread.daemon = 1
        thread.start()
    
    def stopVideo(self):
        global videoOnPlay
        videoOnPlay=0
