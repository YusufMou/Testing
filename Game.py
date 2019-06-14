from tkinter import *
import random
import time

# Define ball properties and functions
class Ball:
    def __init__(self, canvas, color, size, paddle, paddlle_b):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle_b = paddlle_b
        self.id = canvas.create_oval(10, 10, size, size, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.xspeed = random.randrange(-3,3)
        self.yspeed = -1
        self.hit_left = False
        self.hit_right = False
        self.player_right = 0
        self.player_left = 0

    #Making ball bounce on edge of canvas
    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        # print (str(pos))
        if pos[1] <= 0:
            self.yspeed = 4
        if pos[3] >= 500:
            self.yspeed = -4
        if pos[0] <= 0:
            self.hit_left = True
            self.player_right += 1
        if pos[2] >= 900:
            self.hit_right = True
            self.player_left += 1
        if self.hit_paddle_right(pos) == True:
            self.yspeed = -3
            self.xspeed = random.randrange(-3,3)
        if self.hit_paddle_left(pos) == True:
        	self.yspeed = 3
        	self.xspeed = random.randrange(-3,3)

    #Making ball bounce on paddle B
    def hit_paddle_right(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    #Making ball bounce on paddle B
    def hit_paddle_left(self, pos):
    	paddle_pos = self.canvas.coords(self.paddle_b.id_b)
    	if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
    		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
    			return True
    	return False

# Define paddle properties and functions
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,100,10,0, fill=color)
        self.canvas.move(self.id, 850, 200)
        self.yspeed = 0
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)

    #Preventing the paddle from going out of the canvas
    def draw(self):
        self.canvas.move(self.id, 0, self.yspeed)
        pos = self.canvas.coords(self.id)
        # print (str(pos))
        if pos[1] <= 0:
            self.yspeed = 0
        if pos[3] >= 500:
            self.yspeed = 0

    #speed of moving paddle A
    def move_down(self, evt):
        self.yspeed = 4
    def move_up(self, evt):
        self.yspeed = -4

class Paddle_b:
    #Properties of paddle B
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id_b = canvas.create_rectangle(0, 100, 10, 0, fill=color)
        self.canvas.move(self.id_b, 50, 200)
        self.yspeed = 0
        self.canvas.bind_all('<KeyPress-w>', self.move_up)
        self.canvas.bind_all('<KeyPress-s>', self.move_down)

    #Preventing the paddle from going out of the canvas
    def draw(self):
        self.canvas.move(self.id_b, 0, self.yspeed)
        pos = self.canvas.coords(self.id_b)
        if pos[1] <= 0:
            self.yspeed = 0
        if pos[3] >= 500:
            self.yspeed = 0
    #speed of moving paddle B
    def move_down(self, evt):
        self.yspeed = 4
    def move_up(self, evt):
        self.yspeed = -4


# Create window and canvas to draw on
tk = Tk()
tk.title("Ball Game")
canvas = Canvas(tk, width=900, height=500, bd=0, bg='white')
canvas.pack()
label = canvas.create_text(5, 5, anchor=NW, text="Score: 0")
tk.update()
paddle = Paddle(canvas, 'blue')
paddle_b = Paddle_b(canvas, 'green')
ball = Ball(canvas, 'red', 25, paddle, paddle_b)

# Animation loop
while ball.hit_right == False and ball.hit_left == False:
    ball.draw()
    paddle.draw()
    paddle_b.draw()
    canvas.itemconfig(label, text="Player 1: "+str(ball.player_left) + " Player 2: " +str(ball.player_right))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# Game Over
sb = canvas.create_text(450, 100, text="Player 1: "+str(ball.player_left)+" Player 2: "+str(ball.player_right), font=("Helvetica", 30))
go_label = canvas.create_text(450,250,text="GAME OVER",font=("Helvetica",30))
tk.update()

tk.mainloop()