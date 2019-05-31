from tkinter import *
import time
master = Tk()

w = Canvas(master, width=900, height=600, bg="blue")
w.pack()

rectangle = w.create_rectangle(50, 20, 150, 80, fill="red")
y = x = 5


for loops in range(500):
    time.sleep(0.025)
    w.move(rectangle, x, y)
    w.update()
master.mainloop()

