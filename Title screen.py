from tkinter import *
root = Tk()
root.title("Perfect Pong")
can = Canvas(root, width=700, height=500, bd=0,)
can.pack()
filename = 'titlescreenbackground.png'
img = PhotoImage(file=filename)
can.create_image(350, 250, image=img)

root.mainloop()