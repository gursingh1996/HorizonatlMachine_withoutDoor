from tkinter import *
import tkinter.font as font
from Libraries.videoPlayer import videoPlayer
from Libraries.serialData import serialData
from Libraries.GPIO import GPIO
 
myTimer = serialData.serialData()
myTimer.initLoop()

btn = GPIO.GPIOPins()
btn.initPins()
btn.beginReading()

root = Tk()     #initialize the root window
root.geometry("1024x600")
root.config(bg='#000CA4')

#variables for widgets
btnHeight=6
btnWidth=12
btnFont = font.Font(family="Segoe UI", size=8, weight='bold')
textFont = font.Font(family="Segoe UI", size=22, weight='bold')
btnTextColor = '#707070'
btnColor = '#F3E82F'

#definition of widgets
# label_videoPannel = Label(root, height=28, width=109)
label_videoPannel = Label(root)

btn_fullScreen = Button(text="FULL SCREEN\nVIEW", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
btn_diagnostics = Button(text="DIAGNOSTICS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
btn_moreParameters = Button(text="MORE\nPARAMETERS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
btn_settings = Button(text="SETTINGS", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
label_pressureText = Label(root, font=textFont, text="PRESSURE: 2200 PSI", bg='#000CA4', fg='#ffffff')

#placement of widgets
paddingX = 25
paddingY = 12
label_videoPannel.grid(rowspan=3, row=0, column=1, columnspan=3, pady=(0,30))
btn_fullScreen.grid(row=0, column=0, padx=paddingX, pady=(15, paddingY))
btn_diagnostics.grid(row=1, column=0, padx=paddingX, pady=paddingY)
btn_moreParameters.grid(row=2, column=0, padx=paddingX, pady=paddingY)
btn_settings.grid(row=3, column=0, padx=paddingX, pady=paddingY)
label_pressureText.grid(row=3, column=2, pady=(5, 0))

myVideoPlayer = videoPlayer.videoPlayer(label_videoPannel)   #use label as area to project video
myVideoPlayer.playVideo()

root.mainloop()     #read all elements in the window



