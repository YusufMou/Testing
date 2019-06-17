from tkinter import *
import os

root = Tk()
root.title("Perfect Pong")
can = Canvas(root, width=700, height=600, bd=0,)
can.pack()
filename = 'C:\\Users\\s448772\\Documents\\GitHub\\Testing\\titlescreenbackground.png'
img = PhotoImage(file=filename)
can.create_image(400, 250, image=img)

def upload(event=None):
	os.system('C:\\Users\\s448772\\Documents\\GitHub\\Testing\\Game.py')

button1 = Button(text = "Start", fg = "Green", borderwidth=.010, command=upload)
button1.pack()

root.mainloop()