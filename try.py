
from tkinter import *
from PIL import Image, ImageTk

mahmudul_root = Tk()

mahmudul_root.geometry("1255x944")
# photo = PhotoImage(file="1.png")

# For Jpg Images

image = Image.open("Assets/Videos/11.jpg")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()



mahmudul_root.mainloop()
