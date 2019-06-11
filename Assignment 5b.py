
# Created by: Yusuf Moussa
# Created on: 09 April 2019
# Created for: ICS3U
# Assignment 5b
# This is the 21 game program.

from tkinter import *
import random

#Window
root = Tk()
root.geometry("500x300")
root.title("21 Game")

#Starting game.
def start():
	global computer1
	global computer2
	global computer3
	global user1
	global user2
	computer1 = random.randint(1,10)
	computer2 = random.randint(1,10)
	computer3 = random.randint(1,10)
	user1 = random.randint(1,10)
	user2 = random.randint(1,10)
	Label(root, text="Your cards numbers: ").grid(row=2, column=1)
	Label(root, text=str(user1) + ",").grid(row=2, column=2)
	Label(root, text=str(user2)).grid(row=2, column=3)
	starting.grid_forget()

#Draw a card
def drawcard():
	global user3
	user3 = random.randint(1,10)
	Label(root, text= "," + str(user3)).grid(row=2, column=4)
	draw.grid_forget()


def check():
	Label(root, text="Computer's cards: ").grid(row=1, column=1)
	Label(root, text=str(computer1) + ",").grid(row=1, column=2)
	Label(root, text=str(computer2) + ",").grid(row=1, column=3)
	Label(root, text=str(computer3)).grid(row=1, column=4)
	checkbut.grid_forget()
	draw.grid_forget()
	addcomp = int(computer1) + int(computer2) + int(computer3)
	adduser = int(user1) + int(user2) + int(user3)
	if user3 == '':
		adduser = int(user1) + int(user2)
	#Label(root, text=str(adduser)).grid(row=101, column=1)
	if addcomp > 21 and adduser > 21:
		Label(root, text="It's a tie").grid(row=100, column=1)
	elif addcomp > 21 and adduser < 21:
		Label(root, text="You win").grid(row=100, column=1)	
	elif addcomp < 21 and adduser > 21:
		Label(root, text="You lose").grid(row=100, column=1)
	elif addcomp > adduser:
		Label(root, text="You lose").grid(row=100, column=1)
	elif adduser > addcomp:
		Label(root, text="You win").grid(row=100, column=1)			

checkbut = Button()
checkbut["text"] = "Check"
checkbut["command"] = check
checkbut.grid(row=3, column=5)

#START BUTTON
starting = Button()
starting ["text"] = "Start"
starting ["command"] = start
starting.grid(row=1, column=5)

#DRAW A CARD BUTTON
draw = Button()
draw ["text"] = "Draw"
draw ["command"] = drawcard
draw.grid(row=2, column=5)
root.mainloop()
