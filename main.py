from tkinter import *
import tkinter.font as font
from Libraries.videoPlayer import videoPlayer
#from Libraries.Machine_operation import machine_operate
#from Libraries.IO_definitions.IO_definitions import *

mainBackgroundColor = '#B1B1B1'

class myApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0)

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)      

        topFrameBgColor = "#F6F6F6"
        topFrame = Frame(self, background=topFrameBgColor)
        middleUpperFrame = Frame(self, background=mainBackgroundColor)
        middleLowerFrame = Frame(self, height=42, width=700, background=mainBackgroundColor)
        bottomFrame = Frame(self)

        topFrame.grid(row=0, column=0)
        middleUpperFrame.grid(row=1, column=0, pady=(16,0))
        middleLowerFrame.grid_propagate(0)          #donot change size of frame when its content is changed
        middleLowerFrame.grid(row=2, column=0, padx=(0,17), pady=(19,0))       #0,17
        bottomFrame.grid(row=3, column=0)

        self.logoImg = PhotoImage(file="Assets/Icons/logo.png")
        logoLabel = Label(topFrame, image=self.logoImg, background=topFrameBgColor)
        machineNameFont = font.Font(family="Segoe UI", size=28, weight='bold')
        machineNameLabel = Label(topFrame, text="HMU-3000", font=machineNameFont, fg="#6B6B6B", background=topFrameBgColor)
        dateAndTimeFrame = Frame(topFrame, background=topFrameBgColor)
        dateTimeFont = font.Font(family="Segoe UI", size=10, weight='bold')
        dateLabel = Label(dateAndTimeFrame, text="25-Dec-2021", background=topFrameBgColor, font=dateTimeFont, fg="#6B6B6B")
        timeLabel = Label(dateAndTimeFrame, text="02:30 p.m.", background=topFrameBgColor, font=dateTimeFont, fg="#6B6B6B")

        logoLabel.grid(row=0, column=0, padx=(20,0))
        machineNameLabel.grid(row=0, column=1, padx=(132,132), pady=(6,6))
        dateAndTimeFrame.grid(row=0, column=2, padx=(0,10))
        dateLabel.grid(row=0, column=0)
        timeLabel.grid(row=1, column=0, padx=(15,0))

        videLabel = Label(middleUpperFrame, bd=0)
        myVideoPlayer = videoPlayer.videoPlayer(videLabel)   #use label as area to project video
        myVideoPlayer.play()    #creates a thread to play the video
        
        sensorDisplayFrameBgColor = "#EEEEEE"
        sensorDisplayFrame = Frame(middleUpperFrame, background=sensorDisplayFrameBgColor)
        sensorDisplayUpperTextFont = font.Font(family="Segoe UI", size=14, weight='bold')
        sensorDisplayTextColor = "#515151"
        sensorDisplayUnitTextFont = font.Font(family="Segoe UI", size=12, weight='bold')

        pressureFrame = Frame(sensorDisplayFrame, background=sensorDisplayFrameBgColor)
        pressureText = Label(pressureFrame, background=sensorDisplayFrameBgColor, text="Pressure:", font=sensorDisplayUpperTextFont, fg=sensorDisplayTextColor)
        pressureText.grid(row=0, column=0, padx=(5,0))
        pressureValueFrame = Frame(pressureFrame, background="#ffffff", highlightbackground='#000000', highlightthickness=1, height=29, width=220)
        pressureValueFrame.grid(row=1, columnspan=8, padx=(10,0))
        pressureUnitText = Label(pressureFrame, background=sensorDisplayFrameBgColor, text="PSI", font=sensorDisplayUnitTextFont, fg=sensorDisplayTextColor)
        pressureUnitText.grid(row=1, column=9, padx=(3,3))
        pressureFrame.grid(row=0, column=0, pady=(14,0), padx=(2,8))

        voltageFrame = Frame(sensorDisplayFrame, background=sensorDisplayFrameBgColor)
        voltageText = Label(voltageFrame, background=sensorDisplayFrameBgColor, text="Voltage:", font=sensorDisplayUpperTextFont, fg=sensorDisplayTextColor)
        voltageText.grid(row=0, column=0)
        voltageValueFrame = Frame(voltageFrame, background="#ffffff", highlightbackground='#000000', highlightthickness=1, height=30, width=220)
        voltageValueFrame.grid(row=1, columnspan=8, padx=(6,0))
        voltageUnitText = Label(voltageFrame, background=sensorDisplayFrameBgColor, text="V", font=sensorDisplayUnitTextFont, fg=sensorDisplayTextColor)
        voltageUnitText.grid(row=1, column=9, padx=(3,15))
        voltageFrame.grid(row=1, column=0, pady=(5,0), padx=(2,8))

        currentFrame = Frame(sensorDisplayFrame, background=sensorDisplayFrameBgColor)
        currentText = Label(currentFrame, background=sensorDisplayFrameBgColor, text="Motor Current:", font=sensorDisplayUpperTextFont, fg=sensorDisplayTextColor)
        currentText.grid(row=0, column=0, padx=(5,0))
        currentValueFrame = Frame(currentFrame, background="#ffffff", highlightbackground='#000000', highlightthickness=1, height=30, width=220)
        currentValueFrame.grid(row=1, columnspan=8, padx=(6,0))
        currentUnitText = Label(currentFrame, background=sensorDisplayFrameBgColor, text="A", font=sensorDisplayUnitTextFont, fg=sensorDisplayTextColor)
        currentUnitText.grid(row=1, column=9, padx=(3,15))
        currentFrame.grid(row=2, column=0, pady=(5,0), padx=(2,8))

        tempFrame = Frame(sensorDisplayFrame, background=sensorDisplayFrameBgColor)
        tempText = Label(tempFrame, background=sensorDisplayFrameBgColor, text="Oil Temprature:", font=sensorDisplayUpperTextFont, fg=sensorDisplayTextColor)
        tempText.grid(row=0, column=0, padx=(9,0))
        tempValueFrame = Frame(tempFrame, background="#ffffff", highlightbackground='#000000', highlightthickness=1, height=30, width=220)
        tempValueFrame.grid_propagate(0)
        tempValueFrame.grid(row=1, columnspan=8, padx=(10,0))
        tempUnitText = Label(tempFrame, background=sensorDisplayFrameBgColor, text="°C", font=sensorDisplayUnitTextFont, fg=sensorDisplayTextColor)
        tempUnitText.grid(row=1, column=9, padx=(3,15))
        tempFrame.grid(row=3, column=0, pady=(5,24), padx=(2,8))

        videLabel.grid(row=0, column=0, padx=(0,21))
        sensorDisplayFrame.grid(row=0, column=1, padx=(0,18))

        middleLowerFrameFont = font.Font(family="Segoe UI", size=12, weight='bold')
        runTimeText = Label(middleLowerFrame, text="Run Time: ", fg="#515151", font=middleLowerFrameFont, background=mainBackgroundColor)
        runTimeText.grid(row=0, column=0)
        runTimeValue = Label(middleLowerFrame, text="1h 20m", fg="#515151", font=middleLowerFrameFont, background=mainBackgroundColor)
        runTimeValue.grid(row=0, column=1)

        bundleCountText = Label(middleLowerFrame, text="Bundle Count: ", fg="#515151", font=middleLowerFrameFont, background=mainBackgroundColor)
        bundleCountText.grid(row=0, column=2, padx=(355,0))
        bundleCountValue = Label(middleLowerFrame, text="100", fg="#515151", font=middleLowerFrameFont, background=mainBackgroundColor)
        bundleCountValue.grid(row=0, column=3)

        btnFont = font.Font(family="Segoe UI", size=11, weight='bold')
        btnWidth = 15
        btnHeight = 3
        btnDiagnostics = Button(bottomFrame, text="DIAGNOSTICS", height=btnHeight, width=btnWidth, font=btnFont, fg="#515151", bg="#EEEEEE")
        btnDiagnostics.grid(row=0, column=0)
        btnWarnings = Button(bottomFrame, text="WARNINGS", height=btnHeight, width=btnWidth, font=btnFont, fg="#515151", bg="#EEEEEE")
        btnWarnings.grid(row=0, column=1)
        btnErrors = Button(bottomFrame, text="ERRORS", height=btnHeight, width=btnWidth, font=btnFont, fg="#515151", bg="#EEEEEE")
        btnErrors.grid(row=0, column=2)
        btnSettings = Button(bottomFrame, text="SETTINGS", height=btnHeight, width=btnWidth+1, font=btnFont, fg="#515151", bg="#EEEEEE")
        btnSettings.grid(row=0, column=3)


class DiagnosticsPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)
        textFont = font.Font(family="Segoe UI", size=22, weight='bold')
        for i in range(8):
            Label(self, text="Input "+str(i+1)+": ", font=textFont, bg=mainBackgroundColor, fg='#ffffff').grid(row=i, column=0)  
        
        self.icon_btnUnpressed = PhotoImage(file="Assets/Icons/InputUnpressed.png")
        self.icon_btnPressed = PhotoImage(file="Assets/Icons/InputPressed.png")

        iconInput1 = Label(self, image=self.icon_btnUnpressed, bg=mainBackgroundColor)
        iconInput1.grid(row=0, column=1)
        iconInput2 = Label(self, image=self.icon_btnUnpressed, bg=mainBackgroundColor)
        iconInput2.grid(row=1, column=1)
        iconInput3 = Label(self, image=self.icon_btnUnpressed, bg=mainBackgroundColor)
        iconInput3.grid(row=2, column=1)
        iconInput4 = Label(self, image=self.icon_btnUnpressed, bg=mainBackgroundColor)
        iconInput4.grid(row=3, column=1)
        iconInput5 = Label(self, image=self.icon_btnUnpressed, bg=mainBackgroundColor)
        iconInput5.grid(row=4, column=1)
        iconInput6 = Label(self, image=self.icon_btnUnpressed, bg=mainBackgroundColor)
        iconInput6.grid(row=5, column=1)
        iconInput7 = Label(self, image=self.icon_btnUnpressed, bg=mainBackgroundColor)
        iconInput7.grid(row=6, column=1)
        iconInput8 = Label(self, image=self.icon_btnUnpressed, bg=mainBackgroundColor)
        iconInput8.grid(row=7, column=1)
        btn_back = Button(self, text="Back", height=4, width=6, font=font.Font(family="Segoe UI", size=8, weight='bold'), bg='#707070', fg='#F3E82F',
                        command=lambda: master.switch_frame(StartPage))
        btn_back.grid(row=8, column=1)

        iconInputs = [iconInput1, iconInput2, iconInput3, iconInput4, iconInput5, iconInput6, iconInput7, iconInput8]
       # iconsChange = inputExpander.InputIconsDisplay(iconInputs, self.icon_btnUnpressed, self.icon_btnPressed)
        #iconsChange.changeIconsWithInputsLoop()

if __name__ == "__main__":
    #initIO()
    #machine_operate.start_machineOperate_thread()
    app = myApp()
    app.geometry("665x480")     #resolution of the screen being used
    app.config(bg=mainBackgroundColor)
    #app.attributes('-fullscreen', True)        #uncomment to set in full screen
    app.mainloop()