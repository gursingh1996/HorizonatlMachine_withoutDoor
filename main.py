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

        topFrameBgColor = "#F6F6F6"
        topFrame = Frame(self, background=topFrameBgColor)
        middleUpperFrame = Frame(self, background=mainBackgroundColor)
        middleLowerFrame = Frame(self, height=45, width=700, background=mainBackgroundColor)
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
        sensorDisplayValueTextFont = font.Font(family="Segoe UI", size=17, weight='bold')

        pressureFrame = Frame(sensorDisplayFrame, background=sensorDisplayFrameBgColor)
        pressureText = Label(pressureFrame, background=sensorDisplayFrameBgColor, text="Pressure:", font=sensorDisplayUpperTextFont, fg=sensorDisplayTextColor)
        pressureText.grid(row=0, column=0, padx=(5,0))
        pressureValueFrame = Frame(pressureFrame, background="#ffffff", highlightbackground='#000000', highlightthickness=1, height=40, width=220)
        pressureValueFrame.grid(row=1, columnspan=8, padx=(10,0))
        pressureValueFrame.grid_propagate(0)
        pressureValueText = Label(pressureValueFrame, text="2200", fg="black", font=sensorDisplayValueTextFont, width=13, background="#ffffff")
        pressureValueText.grid(pady=(3,0))
        pressureUnitText = Label(pressureFrame, background=sensorDisplayFrameBgColor, text="PSI", font=sensorDisplayUnitTextFont, fg=sensorDisplayTextColor)
        pressureUnitText.grid(row=1, column=9, padx=(3,3))
        pressureFrame.grid(row=0, column=0, pady=(19,0), padx=(2,8))

        voltageFrame = Frame(sensorDisplayFrame, background=sensorDisplayFrameBgColor)
        voltageText = Label(voltageFrame, background=sensorDisplayFrameBgColor, text="Voltage:", font=sensorDisplayUpperTextFont, fg=sensorDisplayTextColor)
        voltageText.grid(row=0, column=0)
        voltageValueFrame = Frame(voltageFrame, background="#ffffff", highlightbackground='#000000', highlightthickness=1, height=40, width=220)
        voltageValueFrame.grid(row=1, columnspan=8, padx=(6,0))
        voltageValueFrame.grid_propagate(0)
        voltageValueText = Label(voltageValueFrame, text="220", fg="black", font=sensorDisplayValueTextFont, width=13, background="#ffffff")
        voltageValueText.grid(pady=(3,0))
        voltageUnitText = Label(voltageFrame, background=sensorDisplayFrameBgColor, text="V", font=sensorDisplayUnitTextFont, fg=sensorDisplayTextColor)
        voltageUnitText.grid(row=1, column=9, padx=(3,15))
        voltageFrame.grid(row=1, column=0, pady=(11,0), padx=(2,8))

        currentFrame = Frame(sensorDisplayFrame, background=sensorDisplayFrameBgColor)
        currentText = Label(currentFrame, background=sensorDisplayFrameBgColor, text="Motor Current:", font=sensorDisplayUpperTextFont, fg=sensorDisplayTextColor)
        currentText.grid(row=0, column=0, padx=(5,0))
        currentValueFrame = Frame(currentFrame, background="#ffffff", highlightbackground='#000000', highlightthickness=1, height=40, width=220)
        currentValueFrame.grid(row=1, columnspan=8, padx=(6,0))
        currentValueFrame.grid_propagate(0)
        currentValueText = Label(currentValueFrame, text="20", fg="black", font=sensorDisplayValueTextFont, width=13, background="#ffffff")
        currentValueText.grid(pady=(3,0))
        currentUnitText = Label(currentFrame, background=sensorDisplayFrameBgColor, text="A", font=sensorDisplayUnitTextFont, fg=sensorDisplayTextColor)
        currentUnitText.grid(row=1, column=9, padx=(3,15))
        currentFrame.grid(row=2, column=0, pady=(11,0), padx=(2,8))

        tempFrame = Frame(sensorDisplayFrame, background=sensorDisplayFrameBgColor)
        tempText = Label(tempFrame, background=sensorDisplayFrameBgColor, text="Oil Temprature:", font=sensorDisplayUpperTextFont, fg=sensorDisplayTextColor)
        tempText.grid(row=0, column=0, padx=(9,0))
        tempValueFrame = Frame(tempFrame, background="#ffffff", highlightbackground='#000000', highlightthickness=1, height=40, width=220)
        tempValueFrame.grid_propagate(0)
        tempValueFrame.grid(row=1, columnspan=8, padx=(10,0))
        tempValueFrame.grid_propagate(0)
        tempValueText = Label(tempValueFrame, text="45", fg="black", font=sensorDisplayValueTextFont, width=13, background="#ffffff")
        tempValueText.grid(pady=(3,0))
        tempUnitText = Label(tempFrame, background=sensorDisplayFrameBgColor, text="°C", font=sensorDisplayUnitTextFont, fg=sensorDisplayTextColor)
        tempUnitText.grid(row=1, column=9, padx=(3,15))
        tempFrame.grid(row=3, column=0, pady=(11,30), padx=(2,8))

        videLabel.grid(row=0, column=0, padx=(0,20))
        sensorDisplayFrame.grid(row=0, column=1, padx=(0,20))

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
        btnHeight = 4
        btnDiagnostics = Button(bottomFrame, activebackground="#EEEEEE", activeforeground="#515151", text="DIAGNOSTICS", height=btnHeight, width=btnWidth, font=btnFont, fg="#515151", bg="#EEEEEE", command=lambda: master.switch_frame(DiagnosticsPage))
        btnDiagnostics.grid(row=0, column=0)
        btnWarnings = Button(bottomFrame, activebackground="#EEEEEE", activeforeground="#515151", text="WARNINGS", height=btnHeight, width=btnWidth, font=btnFont, fg="#515151", bg="#EEEEEE")
        btnWarnings.grid(row=0, column=1)
        btnErrors = Button(bottomFrame, activebackground="#EEEEEE", activeforeground="#515151", text="ERRORS", height=btnHeight, width=btnWidth, font=btnFont, fg="#515151", bg="#EEEEEE")
        btnErrors.grid(row=0, column=2)
        btnSettings = Button(bottomFrame, activebackground="#EEEEEE", activeforeground="#515151", text="SETTINGS", height=btnHeight, width=btnWidth+1, font=btnFont, fg="#515151", bg="#EEEEEE")
        btnSettings.grid(row=0, column=3)


class DiagnosticsPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)
        
        topFrame = Frame(self, background="#E8E8E8", height=80, width=720)
        topFrame.grid(row=0, column=0)
        topFrame.grid_propagate(0)
        Button(topFrame, height=1, width=7, text="BACK", background="#FFFFFF", fg="#6B6B6B", font=font.Font(family="Segoe UI", size=15, weight='bold'), command=lambda: master.switch_frame(StartPage)).grid(row=0, column=0, padx=(14,0), pady=(15,0))
        Label(topFrame, text="DIAGNOSTICS", background="#E8E8E8", fg="#545454", font=font.Font(family="Segoe UI", size=26, weight='bold')).grid(row=0, column=1, padx=(130,0), pady=(11,0))
        middleFrame = Frame(self, background="#FCFCFC", height=383, width=691, highlightbackground='#000000', highlightthickness=1)
        middleFrame.grid(row=1, column=0, padx=(10,10))
        middleFrame.grid_propagate(0)

        headingFrame = Frame(middleFrame)
        headingFrame.grid(row=0, column=0)
        Label(headingFrame, text="INPUT NUMBER", relief=GROOVE, font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=0, ipadx=5)
        Label(headingFrame, text="NAME", relief=GROOVE, font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=1, ipadx=190)
        Label(headingFrame, text="STATUS", relief=GROOVE, font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=2, ipadx=37)

        detailsCanvas = Canvas(middleFrame, height=330, width=665, background="#FCFCFC", highlightthickness=0)
        detailsCanvas.grid(row=1, column=0, pady=(20,0))
        detailsScroll = Scrollbar(middleFrame, orient=VERTICAL, command=detailsCanvas.yview)
        detailsScroll.grid(row=1, column=1, sticky=NS)
        detailsCanvas.config(yscrollcommand=detailsScroll.set)
        detailsCanvas.bind("<Configure>", lambda e: detailsCanvas.configure(scrollregion=detailsCanvas.bbox("all")))
        detailsFrame = Frame(detailsCanvas, background="#FCFCFC")
        detailsCanvas.create_window((0,0), window=detailsFrame, anchor="nw")

        displayInputs=[
            "LIMIT - UPPER PLATE DOWN",
            "LIMIT - UPPER PLATE UP",
            "LIMIT - LOCK APPLIED",
            "LIMIT - LOCK NOT APPLIED",
            "LIMIT - LOWER PLATE FORWARD",
            "LIMIT - LOWER PLATE BACKWARD",
            "LIMIT - BALE OUT PLATE UP",
            "LIMIT - BALE OUT PLATE DOWN",
            "BUTTON - START",
            "BUTTON - STOP",
            "BUTTON - BALE OUT PLATE DOWN"
        ]
        self.iconPressed = PhotoImage(file="Assets/Icons/InputBtnPressed.png")
        iconInputsLabel = [0]*11
        for i in range(11):
            Label(detailsFrame, text=i+1, fg="#4B4B4B", background="#FCFCFC", font=font.Font(family="Malgun Gothic", size=14, weight='bold')).grid(row=i, column=0, padx=(43,43))
            Label(detailsFrame, text=displayInputs[i], fg="#4B4B4B", background="#FCFCFC", font=font.Font(family="Malgun Gothic", size=14, weight='bold')).grid(row=i, column=1, pady=(5,5), sticky="w", padx=(0,145))
            iconInputsLabel[i] = Label(detailsFrame, background="#FCFCFC", image=self.iconPressed)
            iconInputsLabel[i].grid(row=i, column=3)

        lowerFrame = Frame(self)
        lowerFrame.grid(row=2, column=0)
        btnInputs = Button(lowerFrame, activebackground="#01FFBA", activeforeground="#4B4B4B", height=1, width=10, text="INPUTS", background="#01FFBA", fg="#4B4B4B", font=font.Font(family="Malgun Gothic", size=12, weight='bold'))
        btnInputs.grid(row=0, column=0)
        btnOutputs = Button(lowerFrame, activebackground="#F8F8F8", activeforeground="#4B4B4B", height=1, width=10, text="OUTPUTS", background="#F8F8F8", fg="#4B4B4B", font=font.Font(family="Malgun Gothic", size=12, weight='bold'))
        btnOutputs.grid(row=0, column=1)

        # iconInputs = [iconInput1, iconInput2, iconInput3, iconInput4, iconInput5, iconInput6, iconInput7, iconInput8]
       # iconsChange = inputExpander.InputIconsDisplay(iconInputs, self.icon_btnUnpressed, self.icon_btnPressed)
        #iconsChange.changeIconsWithInputsLoop()

if __name__ == "__main__":
    #initIO()
    #machine_operate.start_machineOperate_thread()
    app = myApp()
    app.geometry("720x500")     #resolution of the screen being used
    app.config(bg=mainBackgroundColor)
    # app.attributes('-fullscreen', True)        #uncomment to set in full screen
    app.mainloop()