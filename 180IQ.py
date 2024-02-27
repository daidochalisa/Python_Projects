from tkinter import *
import time
import random

def easymode():
    hardmode_label.pack_forget()
    easymode_label.pack(side = TOP, anchor = S)
    easymode_label.config(text = str(random.randint(1000,9999))+ "="+ str(random.randint(10,99)))


def hardmode():
    easymode_label.pack_forget()
    hardmode_label.pack(side = TOP, anchor = S)
    hardmode_label.config(text = str(random.randint(10000, 99999))+ "="+ str(random.randint(100,999)))

def countdown(t):
    if t > 0 and stopped is False:
        time_label.config(text = t)
        window.after(1000,lambda: countdown(t-1))
    elif t == 0:
        time_label.config(text="TIME OUT!", fg ="red")

def start():
    global stopped
    stopped = False
    countdown(60)
def stop():
    global stopped
    stopped = True
    time_label.config(text = 60)

window = Tk()
window.title('180IQ GAME')
window.geometry("650x300")
window.resizable(False,False)

hardmode_label = Label(window, fg = "blue", font = ('Arial', 35), bg = '#c9c9c4', width = 100, height = 2)

easymode_label = Label(window, fg = "blue", font = ('Arial', 35), bg = '#c9c9c4', width = 100, height = 2)

time_label = Label(window, text = 60, fg = "green", font = ('Arial', 35))
time_label.pack(side = TOP, anchor = E)

frame_easyhard = Frame(window)
frame_easyhard.pack()
frame_easyhard.place(x = 0, y = 236)
frame_resetcountingdown = Frame(window)
frame_resetcountingdown.pack()
frame_resetcountingdown.place(x=325,y= 236)

easymode_start = Button(frame_easyhard, text = "Start (Easy Mode)", command = easymode, font = ('Arial', 12), bg = "yellow", height = 1, width = 35)
easymode_start.pack(expand = True)

hardmode_start = Button(frame_easyhard, text = "Start (Hard Mode)", command = hardmode, font = ('Arial', 12), bg = "gold", height = 1, width = 35)
hardmode_start.pack(expand = True)

start_button = Button(frame_resetcountingdown, text = "Counting down...", command = start, font = ('Arial', 12), bg = "green", height = 1, width = 35)
start_button.pack(expand = True)

stop_button = Button(frame_resetcountingdown, text = "Reset", command = stop, font = ('Arial', 12), bg = "blue", height = 1, width = 35)
stop_button.pack(fill = "both", expand = True)

#window.update()
#windowwidth = window.winfo_width()
#windowheight = window.winfo_height()
#screenwidth = window.winfo_screenwidth()
#screenheight = window.winfo_screenheight()
#x = int((screenwidth/2) - (windowwidth/2))
#y = int((screenheight/2) - (screenwidth/2))
#window.geometry(f"{windowwidth}x{windowheight}+{x}+{y}")

window.mainloop()


