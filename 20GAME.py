from tkinter import *
import math
#import random

def start():
    global accumulate
    accumulate = 0
    num_counted.config(text = 0)
    whose_turn.config(text = "Player A's Turn")

accumulate = 0
def buttonpress(num):
    global accumulate
    accumulate += num
    if whose_turn['text'] == "Player A's Turn" and accumulate < 20:
        num_counted.config(text = accumulate)
        whose_turn.config(text = "Player B's Turn")
    elif whose_turn['text'] == "Player A's Turn" and accumulate >= 20:
        num_counted.config(text=accumulate)
        whose_turn.config(text="You lose! Player B wins!")
    elif whose_turn['text'] == "Player B's Turn" and accumulate < 20:
        num_counted.config(text=accumulate)
        whose_turn.config(text="Player A's Turn")
    elif whose_turn['text'] == "Player B's Turn" and accumulate >= 20:
        num_counted.config(text=accumulate)
        whose_turn.config(text="You lose! Player A wins!")

def quit():
    window.quit()

window = Tk()
window.title("The 20 Game")
window.config(background= "#d3d3d3")
#window.geometry("1000x1000")
window.resizable(False,False)

#players = ["A", "B"]

whose_turn = Label(window, text = "Player A's Turn", font = ('Arial', 36, 'bold'), bg = "#d3d3d3")
#don't forget to add the command here
whose_turn.pack(side = TOP)
num_counted = Label(window, text = 0, font = ('Arial', 72, 'bold'), bg = "blue", width = 15, relief = RAISED, bd = 5)
num_counted.pack()
#num_counted.place(x = ((window.winfo_width()/2) - (num_counted.winfo_width()/2)), y = ((window.winfo_height()/2) - (num_counted.winfo_height()/2)))
frame_num = Frame(window).pack()
#do not forget to add the command for each button
button3 = Button(frame_num, text = 3, font = ('Arial', 48, 'bold'), bg = "purple", command = lambda: buttonpress(3))
button3.pack(side = RIGHT, anchor = S)
button2 = Button(frame_num, text = 2, font = ('Arial', 48, 'bold'), bg = "violet", command = lambda: buttonpress(2))
button2.pack(side = RIGHT, anchor = S)
button1 = Button(frame_num, text = 1, font = ('Arial', 48, 'bold'), bg = "pink", command = lambda: buttonpress(1))
button1.pack(side = RIGHT, anchor = S)

#do not forget to assign the commands for newgame
frame_gamemanager = Frame(window).pack()
newgame = Button(frame_gamemanager, text = "New Game", font = ('Arial', 24, 'bold'), bg = "green", command = start)
newgame.pack(fill = "both")
quitgame = Button(frame_gamemanager, text = "Quit", font = ('Arial', 24, 'bold'), bg = "red", command = quit)
quitgame.pack(fill = "both")

window.mainloop()