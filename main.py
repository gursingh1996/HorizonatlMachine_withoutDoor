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
        self.switch_frame(DiagnosticsOutputsPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0)

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)     
        mainFrame = Frame(self, height=480, width=800, background=mainBackgroundColor)
        mainFrame.grid()
        mainFrame.grid_propagate(0)
        mainFrame.columnconfigure(0, weight=1)

        topFrameBgColor = "#F6F6F6"
        topFrame = Frame(mainFrame, background=topFrameBgColor)
        topFrame.grid(row=0, column=0, sticky="new")
        topFrame.columnconfigure(0, weight=1)
        topFrame.columnconfigure(1, weight=1)
        topFrame.columnconfigure(1, weight=1)
        self.logoImg = PhotoImage(file="Assets/Icons/logo.png")
        Label(topFrame, image=self.logoImg, background=topFrameBgColor).grid(row=0, column=0, sticky="w", padx=(20,0))
        Label(topFrame, text="HMU-3000", font=font.Font(family="Malgun Gothic", size=24, weight='bold'), fg="#6B6B6B", background=topFrameBgColor).grid(row=0, column=1, sticky="w", pady=(9,9))
        dateAndTimeFrame = Frame(topFrame, background=topFrameBgColor)
        dateAndTimeFrame.grid(row=0, column=2, sticky="e", padx=(0,10))
        dateLabel = Label(dateAndTimeFrame, text="25-Dec-2021", background=topFrameBgColor, font=font.Font(family="Segoe UI", size=10, weight='bold'), fg="#6B6B6B")
        dateLabel.grid(row=0, column=0)
        timeLabel = Label(dateAndTimeFrame, text="02:30 p.m.", background=topFrameBgColor, font=font.Font(family="Segoe UI", size=10, weight='bold'), fg="#6B6B6B")
        timeLabel.grid(row=1, column=0, padx=(15,0))

        middleUpperFrame = Frame(mainFrame, background=mainBackgroundColor)
        middleUpperFrame.grid(row=1, column=0, sticky="ew", pady=(16,0))
        middleUpperFrame.columnconfigure(0, weight=1)
        middleUpperFrame.columnconfigure(1, weight=1)
        videLabel = Label(middleUpperFrame, bd=0)
        myVideoPlayer = videoPlayer.videoPlayer(videLabel)   #use label as area to project video
        myVideoPlayer.play()    #creates a thread to play the video
        videLabel.grid(row=0, column=0, sticky="w")
        sensorDisplayFrameBgColor = "#EEEEEE"
        sensorDisplayFrame = Frame(middleUpperFrame, background=sensorDisplayFrameBgColor, highlightbackground="#707070", highlightthickness=1)
        sensorDisplayFrame.grid(row=0, column=1, sticky="nsw")

        sensorDisplayUpperTextFont = font.Font(family="Malgun Gothic", size=10, weight='bold')
        sensorDisplayUnitTextFont = font.Font(family="Malgun Gothic", size=11, weight='bold')
        sensorDisplayValueTextFont = font.Font(family="Malgun Gothic", size=14, weight='bold')

        Label(sensorDisplayFrame, background=sensorDisplayFrameBgColor, text="PRESSURE:", font=sensorDisplayUpperTextFont, fg="#515151").grid(row=0, column=0, sticky="w", padx=(8,0), pady=(12,0))
        Label(sensorDisplayFrame, background="#ffffff", font=font.Font(family="Malgun Gothic", size=1), highlightbackground='#000000', highlightthickness=1, height=10, width=200).grid(row=1, column=0, padx=(10,0))
        pressureValueText = Label(sensorDisplayFrame, text="2200", fg="black", font=sensorDisplayValueTextFont, background="#ffffff")
        pressureValueText.grid(row=1, column=0, padx=(10,0))
        Label(sensorDisplayFrame, background=sensorDisplayFrameBgColor, text="PSI", font=sensorDisplayUnitTextFont, fg="#515151").grid(row=1, column=1, padx=(3,8))

        Label(sensorDisplayFrame, background=sensorDisplayFrameBgColor, text="VOLTAGE:", font=sensorDisplayUpperTextFont, fg="#515151").grid(row=2, column=0, sticky="w", padx=(8,0), pady=(5,0))
        Label(sensorDisplayFrame, background="#ffffff", font=font.Font(family="Malgun Gothic", size=1), highlightbackground='#000000', highlightthickness=1, height=10, width=200).grid(row=3, column=0, padx=(10,0))
        voltageValueText = Label(sensorDisplayFrame, text="240", fg="black", font=sensorDisplayValueTextFont, background="#ffffff")
        voltageValueText.grid(row=3, column=0, padx=(10,0))
        Label(sensorDisplayFrame, background=sensorDisplayFrameBgColor, text="V", font=sensorDisplayUnitTextFont, fg="#515151").grid(row=3, column=1, padx=(3,8))

        Label(sensorDisplayFrame, background=sensorDisplayFrameBgColor, text="MOTOR CURRENT:", font=sensorDisplayUpperTextFont, fg="#515151").grid(row=4, column=0, sticky="w", padx=(8,0), pady=(5,0))
        Label(sensorDisplayFrame, background="#ffffff", font=font.Font(family="Malgun Gothic", size=1), highlightbackground='#000000', highlightthickness=1, height=10, width=200).grid(row=5, column=0, padx=(10,0))
        currentValueText = Label(sensorDisplayFrame, text="30", fg="black", font=sensorDisplayValueTextFont, background="#ffffff")
        currentValueText.grid(row=5, column=0, padx=(10,0))
        Label(sensorDisplayFrame, background=sensorDisplayFrameBgColor, text="A", font=sensorDisplayUnitTextFont, fg="#515151").grid(row=5, column=1, padx=(3,8))

        Label(sensorDisplayFrame, background=sensorDisplayFrameBgColor, text="OIL TEMPRATURE:", font=sensorDisplayUpperTextFont, fg="#515151").grid(row=6, column=0, sticky="w", padx=(8,0), pady=(7,0))
        Label(sensorDisplayFrame, background="#ffffff", font=font.Font(family="Malgun Gothic", size=1), highlightbackground='#000000', highlightthickness=1, height=10, width=200).grid(row=7, column=0, padx=(10,0))
        tempratureValueText = Label(sensorDisplayFrame, text="45", fg="black", font=sensorDisplayValueTextFont, background="#ffffff")
        tempratureValueText.grid(row=7, column=0, padx=(10,0))
        Label(sensorDisplayFrame, background=sensorDisplayFrameBgColor, text="??C", font=sensorDisplayUnitTextFont, fg="#515151").grid(row=7, column=1, padx=(3,8))

        mainFrame.rowconfigure(2, weight=1)
        midLowerFrame = Frame(mainFrame, background=mainBackgroundColor)
        midLowerFrame.grid(row=2, column=0, sticky="sew")
        midLowerFrame.columnconfigure(0, weight=1)
        midLowerFrame.columnconfigure(1, weight=1)
        middleLowerFont = font.Font(family="Malgun Gothic", size=12, weight='bold')
        runTimeValue = Label(midLowerFrame, text="Run Time: 1h 20m", fg="#515151", font=middleLowerFont, background=mainBackgroundColor)
        runTimeValue.grid(row=0, column=0, sticky="w", padx=(5,0))
        bundleCountValue = Label(midLowerFrame, text="Bundle Count: 10000", fg="#515151", font=middleLowerFont, background=mainBackgroundColor)
        bundleCountValue.grid(row=0, column=1, sticky="e", padx=(0,10))

        mainFrame.rowconfigure(3, weight=1)
        bottomFrame = Frame(mainFrame, height=60)
        bottomFrame.grid(row=3, column=0, sticky="sew")
        bottomFrame.grid_propagate(0)
        bottomFrame.rowconfigure(0, weight=1)
        for i in range(4):
            bottomFrame.columnconfigure(i, weight=1)
        
        btnFont = font.Font(family="Malgun Gothic", size=11, weight='bold')
        Button(bottomFrame, activebackground="#EEEEEE", activeforeground="#515151", text="DIAGNOSTICS", font=btnFont, fg="#515151", bg="#EEEEEE", command=lambda: master.switch_frame(DiagnosticsInputsPage)).grid(row=0, column=0, sticky="nsew")
        Button(bottomFrame, activebackground="#EEEEEE", activeforeground="#515151", text="WARNINGS", font=btnFont, fg="#515151", bg="#EEEEEE").grid(row=0, column=1, sticky="nsew")
        Button(bottomFrame, activebackground="#EEEEEE", activeforeground="#515151", text="ERRORS", font=btnFont, fg="#515151", bg="#EEEEEE").grid(row=0, column=2, sticky="nsew")
        Button(bottomFrame, activebackground="#EEEEEE", activeforeground="#515151", text="PARAMETERS", font=btnFont, fg="#515151", bg="#EEEEEE", command=lambda: master.switch_frame(ParametersPage)).grid(row=0, column=3, sticky="nsew")

        

class DiagnosticsInputsPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)

        mainFrame = Frame(self, height=480, width=800, background=mainBackgroundColor)
        mainFrame.grid()
        mainFrame.grid_propagate(0)
        mainFrame.columnconfigure(0, weight=1)
        
        topFrame = Frame(mainFrame, background="#E8E8E8")
        topFrame.grid(row=0, column=0, sticky="new")
        for i in range(3):
            topFrame.columnconfigure(i, weight=1)
        
        btnFrame = Frame(topFrame, height=40, width=90)
        btnFrame.grid(row=0, column=0, sticky="w", padx=(10,0))
        btnFrame.grid_propagate(0)
        btnFrame.rowconfigure(0, weight=1)
        btnFrame.columnconfigure(0, weight=1)
        self.backIcon = PhotoImage(file="Assets/Icons/backIcon.png")
        Button(btnFrame, text="  ", image=self.backIcon, compound="left", activebackground="#FFFFFF", activeforeground="#6B6B6B", background="#FFFFFF", fg="#6B6B6B", font=font.Font(family="Malgun Gothic", size=11, weight='bold'), command=lambda: master.switch_frame(StartPage)).grid(sticky="nsew")
        Label(topFrame, text="DIAGNOSTICS", background="#E8E8E8", fg="#545454", font=font.Font(family="Malgun Gothic", size=18, weight='bold')).grid(row=0, column=1, sticky="w", pady=(8,8), padx=(70,0))

        mainFrame.rowconfigure(1, weight=500)
        middleFrame = Frame(mainFrame, background="#FCFCFC", highlightbackground='#000000', highlightthickness=1)
        middleFrame.grid(row=1, column=0, padx=(10,10), sticky="nsew")
        middleFrame.rowconfigure(0, weight=1)
        middleFrame.columnconfigure(0, weight=1)
        headingFrame = Frame(middleFrame, bg="#FCFCFC")
        headingFrame.grid(row=0, column=0, sticky="new")
        headingFrame.columnconfigure(0, weight=1)
        headingFrame.columnconfigure(2, weight=50)
        headingFrame.columnconfigure(4, weight=10)
        Label(headingFrame, text="INPUT No.", fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=0)
        Frame(headingFrame, bg="#6B6B6B", height=20, width=2).grid(row=0, column=1, sticky="n")
        Label(headingFrame, text="INPUT NAME", fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=2)
        Frame(headingFrame, bg="#6B6B6B", height=20, width=2).grid(row=0, column=3, sticky="n")
        Label(headingFrame, text="STATUS", fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=4, sticky="w", padx=(30,0))

        middleLowerFrame = Frame(middleFrame, background="#FCFCFC")
        middleLowerFrame.grid(row=1, column=0)
        detailsCanvas = Canvas(middleLowerFrame, height=335, width=753, background="#FCFCFC", highlightthickness=0)
        detailsCanvas.grid(row=0, column=0, pady=(0,5))
        detailsScroll = Scrollbar(middleLowerFrame, width=18, elementborderwidth=2, activebackground=mainBackgroundColor, bg=mainBackgroundColor, bd=0, highlightbackground="#E8E8E8", highlightthickness=3, troughcolor="#E8E8E8", orient=VERTICAL, command=detailsCanvas.yview)
        detailsScroll.grid(row=0, column=1, sticky=NS)
        detailsCanvas.config(yscrollcommand=detailsScroll.set)
        detailsCanvas.bind("<Configure>", lambda e: detailsCanvas.configure(scrollregion=detailsCanvas.bbox("all")))
        detailsFrame = Frame(detailsCanvas, background="#FCFCFC")
        detailsCanvas.create_window((0,0), window=detailsFrame, anchor="nw")

        displayInputs=[
            "LIMIT - UPPER PLATE DOWN",
            "LIMIT - UPPER PLATE UP",
            "LIMIT - LOCK APPLIED",
            "LIMIT - LOCK REMOVED",
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
            Label(detailsFrame, text=i+1, fg="#4B4B4B", background="#FCFCFC", font=font.Font(family="Malgun Gothic", size=13, weight='bold')).grid(row=i, column=0, padx=(32,32))
            Label(detailsFrame, text=displayInputs[i], fg="#4B4B4B", background="#FCFCFC", font=font.Font(family="Malgun Gothic", size=13, weight='bold')).grid(row=i, column=1, padx=(5,0), pady=(5,5), sticky="w")
            iconInputsLabel[i] = Label(detailsFrame, background="#FCFCFC", image=self.iconPressed)
            iconInputsLabel[i].grid(row=i, column=3, padx=(216,0))

        mainFrame.rowconfigure(2, weight=1)
        lowerFrame = Frame(mainFrame, bg=mainBackgroundColor, height=42)
        lowerFrame.grid(row=2, column=0, sticky="sew")
        lowerFrame.columnconfigure(0, weight=1)
        lowerFrame.columnconfigure(1, weight=1)
        lowerFrame.rowconfigure(0, weight=1)
        lowerFrame.grid_propagate(0)
        Button(lowerFrame, relief=SUNKEN, activebackground="#01FFBA", activeforeground="#4B4B4B", width=10, text="INPUTS", background="#01FFBA", fg="#4B4B4B", font=font.Font(family="Malgun Gothic", size=12, weight='bold')).grid(row=0, column=0, sticky="nse")
        Button(lowerFrame, activebackground="#F8F8F8", activeforeground="#4B4B4B", width=10, text="OUTPUTS", background="#F8F8F8", fg="#4B4B4B", font=font.Font(family="Malgun Gothic", size=12, weight='bold'), command=lambda: master.switch_frame(DiagnosticsOutputsPage)).grid(row=0, column=1, sticky="nsw")


        # iconInputs = [iconInput1, iconInput2, iconInput3, iconInput4, iconInput5, iconInput6, iconInput7, iconInput8]
       # iconsChange = inputExpander.InputIconsDisplay(iconInputs, self.icon_btnUnpressed, self.icon_btnPressed)
        #iconsChange.changeIconsWithInputsLoop()

class DiagnosticsOutputsPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)
        
        mainFrame = Frame(self, height=480, width=800, background=mainBackgroundColor)
        mainFrame.grid()
        mainFrame.grid_propagate(0)
        mainFrame.columnconfigure(0, weight=1)
        
        topFrame = Frame(mainFrame, background="#E8E8E8")
        topFrame.grid(row=0, column=0, sticky="new")
        for i in range(3):
            topFrame.columnconfigure(i, weight=1)
        
        btnFrame = Frame(topFrame, height=40, width=90)
        btnFrame.grid(row=0, column=0, sticky="w", padx=(10,0))
        btnFrame.grid_propagate(0)
        btnFrame.rowconfigure(0, weight=1)
        btnFrame.columnconfigure(0, weight=1)
        self.backIcon = PhotoImage(file="Assets/Icons/backIcon.png")
        Button(btnFrame, text="  ", image=self.backIcon, compound="left", activebackground="#FFFFFF", activeforeground="#6B6B6B", background="#FFFFFF", fg="#6B6B6B", font=font.Font(family="Malgun Gothic", size=11, weight='bold'), command=lambda: master.switch_frame(StartPage)).grid(sticky="nsew")
        Label(topFrame, text="DIAGNOSTICS", background="#E8E8E8", fg="#545454", font=font.Font(family="Malgun Gothic", size=18, weight='bold')).grid(row=0, column=1, sticky="w", pady=(8,8), padx=(70,0))

        mainFrame.rowconfigure(1, weight=500)
        middleFrame = Frame(mainFrame, background="#FCFCFC", highlightbackground='#000000', highlightthickness=1)
        middleFrame.grid(row=1, column=0, padx=(10,10), sticky="nsew")
        middleFrame.rowconfigure(0, weight=1)
        middleFrame.columnconfigure(0, weight=1)
        headingFrame = Frame(middleFrame, bg="#FCFCFC")
        headingFrame.grid(row=0, column=0, sticky="new")
        headingFrame.columnconfigure(0, weight=1)
        headingFrame.columnconfigure(2, weight=50)
        headingFrame.columnconfigure(4, weight=10)
        Label(headingFrame, text="OUTPUT No.", fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=0)
        Frame(headingFrame, bg="#6B6B6B", height=20, width=2).grid(row=0, column=1, sticky="n")
        Label(headingFrame, text="OUTPUT NAME", fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=2)
        Frame(headingFrame, bg="#6B6B6B", height=20, width=2).grid(row=0, column=3, sticky="n")
        Label(headingFrame, text="STATUS", fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=4, sticky="w", padx=(30,0))

        middleLowerFrame = Frame(middleFrame, background="#FCFCFC")
        middleLowerFrame.grid(row=1, column=0)
        detailsCanvas = Canvas(middleLowerFrame, height=335, width=753, background="#FCFCFC", highlightthickness=0)
        detailsCanvas.grid(row=0, column=0, pady=(0,5))
        detailsScroll = Scrollbar(middleLowerFrame, width=18, elementborderwidth=2, activebackground=mainBackgroundColor, bg=mainBackgroundColor, bd=0, highlightbackground="#E8E8E8", highlightthickness=3, troughcolor="#E8E8E8", orient=VERTICAL, command=detailsCanvas.yview)
        detailsScroll.grid(row=0, column=1, sticky=NS)
        detailsCanvas.config(yscrollcommand=detailsScroll.set)
        detailsCanvas.bind("<Configure>", lambda e: detailsCanvas.configure(scrollregion=detailsCanvas.bbox("all")))
        detailsFrame = Frame(detailsCanvas, background="#FCFCFC")
        detailsCanvas.create_window((0,0), window=detailsFrame, anchor="nw")

        displayOutputs=[
            "MOTOR",
            "COIL - UPPER PLATE DOWN",
            "COIL - UPPER PLATE UP",
            "COIL - LOCK APPLY",
            "COIL - LOCK REMOVE",
            "COIL - LOWER PLATE FORWARD",
            "COIL - LOWER PLATE BACKWARD",
            "COIL - BALE OUT PLATE UP",
            "COIL - BALE OUT PLATE DOWN",
        ]
        self.iconActive = PhotoImage(file="Assets/Icons/OutputOn.png")
        iconOutputsLabel = [0]*9
        for i in range(9):
            Label(detailsFrame, text=i+1, fg="#4B4B4B", background="#FCFCFC", font=font.Font(family="Malgun Gothic", size=13, weight='bold')).grid(row=i, column=0, padx=(41,41))
            Label(detailsFrame, text=displayOutputs[i], fg="#4B4B4B", background="#FCFCFC", font=font.Font(family="Malgun Gothic", size=13, weight='bold')).grid(row=i, column=1, padx=(8,0), pady=(5,5), sticky="w")
            iconOutputsLabel[i] = Label(detailsFrame, background="#FCFCFC", image=self.iconActive)
            iconOutputsLabel[i].grid(row=i, column=3, padx=(225,0))

        mainFrame.rowconfigure(2, weight=1)
        lowerFrame = Frame(mainFrame, bg=mainBackgroundColor, height=42)
        lowerFrame.grid(row=2, column=0, sticky="sew")
        lowerFrame.columnconfigure(0, weight=1)
        lowerFrame.columnconfigure(1, weight=1)
        lowerFrame.rowconfigure(0, weight=1)
        lowerFrame.grid_propagate(0)
        Button(lowerFrame, activebackground="#F8F8F8", activeforeground="#4B4B4B", width=10, text="INPUTS", background="#F8F8F8", fg="#4B4B4B", font=font.Font(family="Malgun Gothic", size=12, weight='bold'), command=lambda: master.switch_frame(DiagnosticsInputsPage)).grid(row=0, column=0, sticky="nse")
        Button(lowerFrame, relief=SUNKEN, activebackground="#01FFBA", activeforeground="#4B4B4B", width=10, text="OUTPUTS", background="#01FFBA", fg="#4B4B4B", font=font.Font(family="Malgun Gothic", size=12, weight='bold')).grid(row=0, column=1, sticky="nsw")


        # iconInputs = [iconInput1, iconInput2, iconInput3, iconInput4, iconInput5, iconInput6, iconInput7, iconInput8]
       # iconsChange = inputExpander.InputIconsDisplay(iconInputs, self.icon_btnUnpressed, self.icon_btnPressed)
        #iconsChange.changeIconsWithInputsLoop()

class ParametersPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=mainBackgroundColor)
        
        mainFrame = Frame(self, height=480, width=800, background=mainBackgroundColor)
        mainFrame.grid()
        mainFrame.grid_propagate(0)
        mainFrame.columnconfigure(0, weight=1)
        
        topFrame = Frame(mainFrame, background="#E8E8E8")
        topFrame.grid(row=0, column=0, sticky="new")
        for i in range(3):
            topFrame.columnconfigure(i, weight=1)
        
        btnFrame = Frame(topFrame, height=40, width=90)
        btnFrame.grid(row=0, column=0, sticky="w", padx=(10,0))
        btnFrame.grid_propagate(0)
        btnFrame.rowconfigure(0, weight=1)
        btnFrame.columnconfigure(0, weight=1)
        self.backIcon = PhotoImage(file="Assets/Icons/backIcon.png")
        Button(btnFrame, text="  ", image=self.backIcon, compound="left", activebackground="#FFFFFF", activeforeground="#6B6B6B", background="#FFFFFF", fg="#6B6B6B", font=font.Font(family="Malgun Gothic", size=11, weight='bold'), command=lambda: master.switch_frame(StartPage)).grid(sticky="nsew")
        Label(topFrame, text="PARAMETERS", background="#E8E8E8", fg="#545454", font=font.Font(family="Malgun Gothic", size=18, weight='bold')).grid(row=0, column=1, sticky="w", pady=(8,8), padx=(70,0))

        mainFrame.rowconfigure(1, weight=500)
        middleFrame = Frame(mainFrame, background="#FCFCFC", highlightbackground='#000000', highlightthickness=1)
        middleFrame.grid(row=1, column=0, sticky="nsew")
        middleFrame.rowconfigure(0, weight=1)
        middleFrame.columnconfigure(0, weight=1)
        headingFrame = Frame(middleFrame, bg="#FCFCFC")
        headingFrame.grid(row=0, column=0, sticky="new")
        headingFrame.columnconfigure(0, weight=42)
        headingFrame.columnconfigure(2, weight=10)
        headingFrame.columnconfigure(4, weight=13)
        Label(headingFrame, text="PARAMETER NAME", fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=0)
        Frame(headingFrame, bg="#6B6B6B", height=20, width=2).grid(row=0, column=1, sticky="n")
        Label(headingFrame, text="VALUE", fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=2)
        Frame(headingFrame, bg="#6B6B6B", height=20, width=2).grid(row=0, column=3, sticky="n")
        Label(headingFrame, fg="#6B6B6B", bg="#FCFCFC", font=font.Font(family="Malgun Gothic", size=10, weight='bold')).grid(row=0, column=4, sticky="w", padx=(30,0))

        middleLowerFrame = Frame(middleFrame, background="#FCFCFC")
        middleLowerFrame.grid(row=1, column=0)
        detailsCanvas = Canvas(middleLowerFrame, height=400, width=772, background="#FCFCFC", highlightthickness=0)
        detailsCanvas.grid(row=0, column=0)
        detailsScroll = Scrollbar(middleLowerFrame, width=18, elementborderwidth=2, activebackground=mainBackgroundColor, bg=mainBackgroundColor, bd=0, highlightbackground="#E8E8E8", highlightthickness=3, troughcolor="#E8E8E8", orient=VERTICAL, command=detailsCanvas.yview)
        detailsScroll.grid(row=0, column=1, sticky=NS)
        detailsCanvas.config(yscrollcommand=detailsScroll.set)
        detailsCanvas.bind("<Configure>", lambda e: detailsCanvas.configure(scrollregion=detailsCanvas.bbox("all")))
        detailsFrame = Frame(detailsCanvas, background="#FCFCFC")
        detailsCanvas.create_window((0,0), window=detailsFrame, anchor="nw")

        parameterList = [
            "UPPER PLATE DOWN TIME",
            "UPPER PLATE DOWN MAX PRESSURE"
        ]
        valueFrame = [0]*2
        values = [2000, 4]

        for i in range(2):
            Label(detailsFrame, text=parameterList[i], fg="#4B4B4B", background="#FCFCFC", font=font.Font(family="Malgun Gothic", size=11, weight='bold')).grid(row=i, column=0, sticky="w")
            labelPadLeft=220
            Label(detailsFrame, height=11, width=100, background="#ffffff", highlightbackground="black", highlightthickness=1, font=font.Font(size=1)).grid(row=i, column=1, pady=(8,8), padx=(labelPadLeft,0))
            Label(detailsFrame, background="#ffffff", text=values[i], font=font.Font(family="Malgun Gothic", size=12, weight='bold')).grid(row=i, column=1, padx=(labelPadLeft,0))
            Button(detailsFrame, background="#C5C5C5", activebackground="#C5C5C5", fg="#212121", activeforeground="#212121", height=1, text="CHANGE", font=font.Font(family="Malgun Gothic", size=10, weight='bold'), command=lambda: master.switch_frame(ParameterInputPage)).grid(row=i, column=2, padx=(30,0))

class ParameterInputPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        mainFrame = Frame(self, height=480, width=800, background="#EEEEEE")
        mainFrame.grid()
        mainFrame.grid_propagate(0)
        mainFrame.columnconfigure(0, weight=1)
        headingLabel = Label(mainFrame, fg="#515151", bg="#EEEEEE", text="UPPER PLATE DOWN TIME", font=font.Font(family="Malgun Gothic", size=14, weight='bold'))
        headingLabel.grid(row=0, column=0, pady=(15,0))    #new - north east west
        oldValFrame = Frame(mainFrame, background="#EEEEEE")
        oldValFrame.grid(row=1, column=0, pady=(15,0))
        Label(oldValFrame, text="OLD VALUE: ", fg="#515151", bg="#EEEEEE", font=font.Font(family="Malgun Gothic", size=12, weight='bold')).grid(row=0, column=0)
        oldValLabel = Label(oldValFrame, fg="#515151", bg="#EEEEEE", text="20s", font=font.Font(family="Malgun Gothic", size=12, weight='bold'))
        oldValLabel.grid(row=0, column=1)
        newValFrame = Frame(mainFrame, background="#EEEEEE")
        newValFrame.grid(row=2, column=0, pady=(15,0))
        Label(newValFrame, text="NEW VALUE: ", fg="#515151", bg="#EEEEEE", font=font.Font(family="Malgun Gothic", size=14, weight='bold')).grid(row=0, column=0)
        Label(newValFrame, height=11, width=120, background="#ffffff", highlightbackground="black", highlightthickness=1, font=font.Font(size=1)).grid(row=0, column=1)
        keypadFrame = Frame(mainFrame, background="#EEEEEE", height=240, width=400)
        keypadFrame.grid(row=3, column=0, pady=(32,0))
        keypadFrame.grid_propagate(0)
        for i in range(4):
            keypadFrame.rowconfigure(i, weight=1)
            if i<3: keypadFrame.columnconfigure(i, weight=1)
        keypadVal=1
        btnWidth=8
        for i in range(3):
            for j in range(3):
                Button(keypadFrame, text=keypadVal, activebackground="#ffffff", activeforeground="#515151", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=16, weight='bold')).grid(row=i, column=j, sticky="nsew")
                keypadVal+=1
        Button(keypadFrame, text=".", activebackground="#ffffff", activeforeground="#515151", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=16, weight='bold')).grid(row=3, column=0, sticky="nsew")
        Button(keypadFrame, text="0", activebackground="#ffffff", activeforeground="#515151", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=16, weight='bold')).grid(row=3, column=1, sticky="nsew")
        Button(keypadFrame, text="C", activebackground="#ffffff", activeforeground="#515151", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=16, weight='bold')).grid(row=3, column=2, sticky="nsew")
        mainFrame.rowconfigure(4, weight=1)
        lowerFrame = Frame(mainFrame, background="#B1B1B1")
        lowerFrame.grid(row=4, column=0, sticky="sew")
        lowerFrame.columnconfigure(0, weight=1)
        lowerFrame.columnconfigure(1, weight=1)
        Button(lowerFrame, text="OK", height=2, width=13, activebackground="#ffffff", activeforeground="#515151", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=12, weight='bold'), command=lambda: master.switch_frame(ParametersPage)).grid(row=3, column=0, sticky="e")
        Button(lowerFrame, text="CANCEL", height=2, width=13, activebackground="#ffffff", activeforeground="#515151", fg="#515151", bg="#ffffff", font=font.Font(family="Malgun Gothic", size=12, weight='bold'), command=lambda: master.switch_frame(ParametersPage)).grid(row=3, column=1, sticky="w")

if __name__ == "__main__":
    #initIO()
    #machine_operate.start_machineOperate_thread()
    app = myApp()
    app.geometry("800x480")     #resolution of the screen being used
    app.config(bg=mainBackgroundColor)
    app.config(cursor="none")
    app.attributes('-fullscreen', True)        #uncomment to set in full screen
    app.mainloop()