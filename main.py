from tkinter import *
import tkinter.font as font
from Libraries.videoPlayer import videoPlayer
from Libraries.inputExpander import inputExpander, InputIconsDisplay

updateMachineInputs = inputExpander()
updateMachineInputs.readDataLoop()

mainBackgroundColor = '#000CA4'

class myApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(DiagnosticsPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0)

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)      

        #variables
        btnHeight=6
        btnWidth=12
        btnFont = font.Font(family="Segoe UI", size=8, weight='bold')
        textFont = font.Font(family="Segoe UI", size=22, weight='bold')
        btnTextColor = '#707070'
        btnColor = '#F3E82F'

        btn_frame = Frame(self, highlightbackground='red', highlightthickness=3)
        btn_frame.grid(row=0, column=0) 
        
        btn_fullScreen = Button(btn_frame, text="FULL SCREEN\nVIEW", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor,
                                command=lambda: master.switch_frame(DiagnosticsPage))
        btn_diagnostics = Button(btn_frame, text="DIAGNOSTICS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
        btn_moreParameters = Button(btn_frame, text="MORE\nPARAMETERS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
        btn_settings = Button(btn_frame, text="SETTINGS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)

        btn_fullScreen.grid(row=0)
        btn_diagnostics.grid(row=1)
        btn_moreParameters.grid(row=2)
        btn_settings.grid(row=3)

        video_frame = Frame(self, highlightbackground='yellow', highlightthickness=3, bg=mainBackgroundColor)
        video_frame.grid(row=0, column=1) 

        label_videoPannel = Label(video_frame)
        label_pressureText = Label(video_frame, font=textFont, text="PRESSURE: 2200 PSI", bg=mainBackgroundColor, fg='#ffffff')
        label_videoPannel.grid(row=0)
        label_pressureText.grid(row=1)

        myVideoPlayer = videoPlayer.videoPlayer(label_videoPannel)   #use label as area to project video
        myVideoPlayer.playVideo()

class DiagnosticsPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)
        textFont = font.Font(family="Segoe UI", size=22, weight='bold')
        for i in range(8):
            Label(self, text="Input "+str(i+1)+": ", font=textFont, bg=mainBackgroundColor, fg='#ffffff').grid(row=i, column=0)  
        
        self.icon_btnUnpressed = PhotoImage(file="Assets/Icons/InputUnpressed.png")
        self.icon_btnPressed = PhotoImage(file="Assets/Icons/InputPressed.png")

        iconInput1 = Label(self, image=self.icon, bg=mainBackgroundColor).grid(row=0, column=1)
        iconInput2 = Label(self, image=self.icon, bg=mainBackgroundColor).grid(row=1, column=1)
        iconInput3 = Label(self, image=self.icon, bg=mainBackgroundColor).grid(row=2, column=1)
        iconInput4 = Label(self, image=self.icon, bg=mainBackgroundColor).grid(row=3, column=1)
        iconInput5 = Label(self, image=self.icon, bg=mainBackgroundColor).grid(row=4, column=1)
        iconInput6 = Label(self, image=self.icon, bg=mainBackgroundColor).grid(row=5, column=1)
        iconInput7 = Label(self, image=self.icon, bg=mainBackgroundColor).grid(row=6, column=1)
        iconInput8 = Label(self, image=self.icon, bg=mainBackgroundColor).grid(row=7, column=1)
        
        iconInputs = [iconInput1, iconInput2, iconInput3, iconInput4, iconInput5, iconInput6, iconInput7, iconInput8]
        iconsChange = InputIconsDisplay(iconInputs, self.icon_btnUnpressed, self.icon_btnPressed)
        iconsChange.changeIconsWithInputsLoop()

if __name__ == "__main__":
    app = myApp()
    app.geometry("1024x600")
    app.config(bg=mainBackgroundColor)
    app.mainloop()