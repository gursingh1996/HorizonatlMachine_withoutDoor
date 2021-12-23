#variables
        btnHeight=6
        btnWidth=22
        btnFont = font.Font(family="Segoe UI", size=8, weight='bold')
        btnTextColor = '#707070'
        btnColor = '#F3E82F'
        
        upper_frame = Frame(self, highlightbackground='yellow', highlightthickness=3, bg=mainBackgroundColor, pady=50)
        btn_frame = Frame(self, highlightbackground='red', highlightthickness=3)        #or the lower frame
        values_frame = Frame(upper_frame, highlightbackground='green', highlightthickness=3, bg=mainBackgroundColor)    #inside upper frame on right side

        upper_frame.grid(row=0, column=0) 
        btn_frame.grid(row=1, column=0) 
        
        label_videoPannel = Label(upper_frame)
        myVideoPlayer = videoPlayer.videoPlayer(label_videoPannel)   #use label as area to project video

        btn_fullScreen = Button(btn_frame, text="FULL SCREEN\nVIEW", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
        btn_diagnostics = Button(btn_frame, text="DIAGNOSTICS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor,
                            command=lambda:  master.switch_frame(DiagnosticsPage))
        btn_moreParameters = Button(btn_frame, text="MORE\nPARAMETERS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
        btn_settings = Button(btn_frame, text="SETTINGS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
        
        label_font = font.Font(family="Segoe UI", size=20, weight='bold')
        label_voltage = Label(values_frame, text="Voltage = 220 V", font=label_font, bg=mainBackgroundColor, fg='#ffffff', anchor="w")
        label_current = Label(values_frame, text="Current = 16 A", font=label_font, bg=mainBackgroundColor, fg='#ffffff', anchor="w")
        label_pressure = Label(values_frame, text="Pressure = 2200 PS", font=label_font, bg=mainBackgroundColor, fg='#ffffff', anchor="w")

    #Inside upper frame
        label_videoPannel.grid(row=0, column=0)     
        values_frame.grid(row=0, column=1)
        #inside values frame
        label_voltage.grid(row=0, column=0, ipadx=0, ipady=0)
        label_current.grid(row=1, column=0, ipadx=0, ipady=10)
        label_pressure.grid(row=2, column=0, ipadx=0, ipady=10)
    
    #inside lower frame
        btn_fullScreen.grid(row=0, column=0)
        btn_diagnostics.grid(row=0, column=1)
        btn_moreParameters.grid(row=0, column=2)
        btn_settings.grid(row=0, column=3)        

        myVideoPlayer.play()    #creates a thread to play the video