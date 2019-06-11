from tkinter import *
import time
#Create window
master = Tk()

#Create canvas
w = Canvas(master, width=900, height=600, bg="blue")
w.pack()

#Create ball
# class Ball:
# 	def __init__(self):
		
shape = w.create_oval(0, 0, 20, 20, fill='red')
x = y = 5

#Moving the ball
for ball in range(0 ,100):
  w.move(shape, x, y)
  master.update()
  time.sleep(.01)

# pos = canvas.coords(shape)  
# if pos[1] <= 0:
# 	y = 3
# if pos[3] >= 600:
# 	y = -3
# if pos[0] <= 0:
# 	x = 3
# if pos[2] >= 900:
# 	x = -3

master.mainloop()
# class ball(self):
# 	self.shape = w.create_oval(0, 0, 50, 50, fill='red')
# pos = w.coords(shape)
# if pos[2] >= WIDTH or pos[0] <= 0:
#     speedx *= -1
# if pos[3] >= HEIGHT or pos[1] <= 0:
#     speedy *= -1