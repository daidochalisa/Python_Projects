from tkinter import *
from collections import Counter

num_of_players_list = []
def submit():
    global num_of_players_list
    try:

        if int(number_of_players_entry.get()) < 5:
            number_of_players_label.config(text="Invalid number! This game is for 5 players or more!")
            number_of_players_entry.delete(0, END)
            number_of_players_entry.config(state=NORMAL)
            submit_button.config(state=ACTIVE)
        else:
            for i in range(0, 2):
                num_of_players_list.append(int(number_of_players_entry.get()))
                # The first element will be fixed.
                # So, when at least one player is eliminated, the eligible numbers to be voted out will be not affected.
                # The second element is to monitor how many players are left.

            number_of_players_label.config(text=str(num_of_players_list[0]) + " players left")
            number_of_players_entry.config(state=DISABLED)
            submit_button.config(state=DISABLED)
            voteout_entry.config(state=NORMAL)
            add_button.config(state=ACTIVE)
    except ValueError:
        number_of_players_label.config(text = "Invalid input! Please type the number starting from 5!")

votedout_total = []
pre_max_votes = []
max_votes = []
def add():
    global num_of_players_list
    global pre_max_votes
    global max_votes

    try:
        votedout_player = voteout_entry.get()
        votedout_player = int(votedout_player)


        if max_votes.count(votedout_player) > 0:
            voteout_label.config(text="This player has already been eliminated!")
        elif votedout_player > int(num_of_players_list[0]) or votedout_player == 0:
            voteout_label.config(text="Invalid number! Please enter 1 to " + str(num_of_players_list[0]))
        else:
            voteout_label.config(text="")
            votedout_total.append(votedout_player)

        voteout_entry.delete(0, END)

    except ValueError:
        voteout_label.config(text="Invalid input! You must enter a number" + " 1 to " + str(num_of_players_list[0]))

    if len(votedout_total) == int(num_of_players_list[1]):
        add_button.config(state=DISABLED)
        announcing()

def announcing():
    global votedout_total
    global pre_max_votes
    global max_votes
    global num_of_players_list

    counting_votes = Counter(votedout_total)
    pre_max_votes = max(counting_votes.values())
    max_votes = [key for key, value in counting_votes.items() if value == pre_max_votes]
    #max_votes.append(counting_votes.most_common(1)[0][0])

    if len(max_votes) == 1:
        voteout_label.config(text="Player " + str(max_votes) + " is eliminated!")
        num_of_players_list[1] -= len(max_votes)
        number_of_players_label.config(text=str(num_of_players_list[1]) + " players left")
    elif len(max_votes) >= 2:
        voteout_label.config(text="Players " + str(max_votes) + " are eliminated!")
        num_of_players_list[1] -= len(max_votes)
        number_of_players_label.config(text=str(num_of_players_list[1]) + " players left")

    votedout_total.clear()
    voteout_entry.config(state=NORMAL)
    add_button.config(state=ACTIVE)

    if (num_of_players_list[1] == 2):
        announcing_the_winners_label.config(text="The rest two are the winners!")
        number_of_players_label.config(text="")

def new_game():
    global num_of_players_list
    global votedout_total
    global pre_max_votes
    global max_votes

    num_of_players_list = []
    votedout_total = []
    pre_max_votes = []
    max_votes = []

    announcing_the_winners_label.config(text="")

    voteout_entry.delete(0,END)
    voteout_entry.config(state=DISABLED)

    voteout_label.config(text = "")

    add_button.config(state=DISABLED)

    number_of_players_entry.delete(0,END)
    number_of_players_entry.config(state=NORMAL)

    number_of_players_label.config(text="")

    submit_button.config(state=ACTIVE)

def quit():
    window.quit()

window = Tk()
window.geometry("1200x740")
window.config(background='#66d9ff')
window.resizable(False,False)

game_title_label = Label(window, text = "Vote Out Game", font = ('Consolas',36,'bold'), bg = '#66d9ff').pack(side=TOP, fill = 'both')

announcing_the_winners_label = Label(window, font = ('Consolas',30, 'bold'), height = 2, bg = '#c2d6d6' , fg = 'green')
announcing_the_winners_label.pack(fill = 'both')

VoteOnePlayerOut_label = Label(window, text = "Vote ONE Player Out", font = ('Consolas',30), bg = '#66d9ff')
VoteOnePlayerOut_label.pack(fill = 'both')

voteout_entry = Entry(window, show = '*', state=DISABLED, font = ('Consolas',30))
voteout_entry.pack()

add_button = Button(window, text = "Add", command = add, state=DISABLED, font = ('Consolas',20), height = 1, width = 10, bg = '#ffffb3')
add_button.pack()

voteout_label = Label(window, font = ('Consolas',30), bg = '#c2d6d6', height = 2)
voteout_label.pack(fill = 'both')

HowManyPlayers_label = Label(window, text = "How Many Players?", font = ('Consolas',30), bg = '#66d9ff')
HowManyPlayers_label.pack(fill = 'both')

number_of_players_entry = Entry(window, font = ('Consolas',30))
number_of_players_entry.pack()

submit_button = Button(window, text = "Submit", command = submit, font = ('Consolas',20), height = 1, width = 10, bg = '#ffffb3')
submit_button.pack(side=TOP)

number_of_players_label = Label(window, font = ('Consolas',30),  bg = '#c2d6d6', height = 2)
number_of_players_label.pack(fill = 'both')

#two_buttons_frame = Frame(window, height = 1).pack()

newgame_button = Button(window, text = "New Game", command = new_game, font = ('Consolas',20), width = 10, bg = '#66ffd9')
newgame_button.pack(side = LEFT)

quit_button = Button(window, text = "Quit", command = quit, font = ('Consolas',20), width = 10, bg = '#ff9999')
quit_button.pack(side = RIGHT)

window.mainloop()