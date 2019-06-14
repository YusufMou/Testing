from tkinter import *
root = Tk()
root.title("Perfect Pong")
can = Canvas(root, width=700, height=600, bd=0,)
can.pack()
filename = 'C:\\Users\\s448772\\Documents\\GitHub\\Testing\\titlescreenbackground.png'
img = PhotoImage(file=filename)
can.create_image(400, 250, image=img)

root.mainloop()