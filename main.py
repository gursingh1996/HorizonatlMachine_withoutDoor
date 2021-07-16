from math import pi
from tkinter import *
import tkinter.font as font
from Libraries.videoPlayer import videoPlayer
 
root = Tk()     #initialize the root window
root.geometry("1024x600")
root.config(bg='#000CA4')

#variables for widgets
btnHeight=2
btnWidth=14
btnFont = font.Font(family="Segoe UI", size=15, weight='bold')
textFont = font.Font(family="Segoe UI", size=25, weight='bold')
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
label_videoPannel.grid(rowspan=3, row=0, column=1, columnspan=3)
btn_fullScreen.grid(row=0, column=0, padx=40, pady=(55, 25))
btn_diagnostics.grid(row=1, column=0, padx=40, pady=25)
btn_moreParameters.grid(row=2, column=0, padx=40, pady=25)
btn_settings.grid(row=3, column=0, padx=40, pady=25)
label_pressureText.grid(row=3, column=3, pady=(35, 0))

myVideoPlayer = videoPlayer.videoPlayer(label_videoPannel)   #use label as area to project video
myVideoPlayer.playVideo()

root.mainloop()     #read all elements in the window