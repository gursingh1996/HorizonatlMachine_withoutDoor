import tkinter as tk  # for Python3
from ..Machine_operation.variables import video_number

import threading
from time import sleep

class videoPlayer():
    last_video_number = video_number
    videoFileLocation = {
        0: "Assets/Frames/Default.png",
        1: "Assets/Frames/Upper-plate-down/",
        2: "Assets/Frames/Lock-apply/",
        3: "Assets/Frames/Lower-plate-forward/",
        4: "Assets/Frames/Lower-plate-backward/",
        5: "Assets/Frames/Lock-out/",
        6: "Assets/Frames/Upper-plate-up/",
        7: "Assets/Frames/Bale-plate-up/",
        8: "Assets/Frames/Bale-plate-down/"
    }
    def __init__(self, label):
        self.label = label

    def load(self):
        exitLoop=0
        while True:
            if videoPlayer.last_video_number==0:
                while videoPlayer.last_video_number==video_number:
                    fileLocation = videoPlayer.videoFileLocation[0]
                    self.frame = tk.PhotoImage(file=fileLocation)
                    try:    #check if frame is available 
                        self.label.config(image=self.frame)
                        self.label.image = self.frame
                    except:     #if frame is changed stop playing video
                        exitLoop=1
                        break
                    sleep(0.05)
                
            else:
                for i in range(15):
                    if videoPlayer.last_video_number != video_number:
                        videoPlayer.last_video_number = video_number
                        break

                    fileLocation = videoPlayer.videoFileLocation[videoPlayer.last_video_number] + str(i) + ".png"
                    self.frame = tk.PhotoImage(file=fileLocation)
                    try:    #check if frame is available 
                        self.label.config(image=self.frame)
                        self.label.image = self.frame
                    except:     #if frame is changed stop playing video
                        exitLoop=1
                        break
                    sleep(0.05)
            
            if exitLoop:    break

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load)
        thread.daemon = 1
        thread.start()