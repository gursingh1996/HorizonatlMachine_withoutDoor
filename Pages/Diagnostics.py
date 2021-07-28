import sys
sys.path.append("../")
from tkinter import *
import tkinter.font as font

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

btn_fullScreen = Button(text="FULL SCREEN\nVIEW", height=btnHeight, width=btnWidth, font=btnFont, bg=btnColor, fg=btnTextColor)
btn_fullScreen.pack()

root.mainloop()     #read all elements in the window