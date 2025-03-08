from tkinter  import *
import random

#create the object
root = Tk()

#set the geometry
root.geometry("300x300")
root.title("Rock Paper Scissor")

# computer input
computer_value = {'0':'Rock','1':'Paper','2':'Scissor'}

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "player")
    l3.config(text = "Computer")
    l4.config(text = "")
    
def disable_button():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
    
#if player choosed rock
def isRock():
    cv = computer_value[str(random.randint(0,2))]
    if cv == "Rock":
        result = "Match Draw"
    elif cv == "Paper":
        result = "Computer Wins"
    else:
        result = "Player Wins"
    l1.config(text = "Rock")
    l3.config(text = cv)
    l4.config(text = result)
    disable_button()

#if player choose paper
def isPaper():
    cv = computer_value[str(random.randint(0,2))]
    if cv == "Paper":
        result = "Match Draw"
    elif cv == "Scissor":
        result = "Computer Wins"
    else:
        result = "Player Wins"
    l1.config(text = "Paper")
    l3.config(text = cv)
    l4.config(text = result)
    disable_button()

#if player choose Scissor
def isScissor():
    cv = computer_value[str(random.randint(0,2))]
    if cv == "Scissor":
        result = "Match Draw"
    elif cv == "Rock":
        result = "Computer wins"
    else:
        result = "Player Wins"
    l1.config(text = "Scissor")
    l3.config(text = cv)
    l4.config(text = result)
    disable_button()
    
#adding the labels,buttons and frames
Label(root,text = "Rock Paper Scissor",font = "normal 20 bold",fg = "blue").pack(pady = 20)
frame = Frame(root)
frame.pack()    

#assigning the labels
l1 = Label(frame,text = "Player",font = 10)
l2 = Label(frame,text = "Vs",font = 15)
l3 = Label(frame,text = "Computer",font = 10)

#using grid
l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=0, column=1, padx=5, pady=5)
l3.grid(row=0, column=2, padx=5, pady=5)

l4 = Label(frame,text = "",font = "normal 10 bold",bg = "blue",width = 15,borderwidth = 2,relief = "solid")
l4.grid(row = 1,column = 0,columnspan = 3 ,pady = 5)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1,text = "Rock",font = 10,width = 7,command = isRock)
b2 = Button(frame1,text = "Paper",font = 10,width = 7,command = isPaper)
b3 = Button(frame1,text = "Scissor",font = 10,width = 7,command = isScissor)

b1.pack(side = LEFT,padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)

#button to reset the game
Button(root,text = "Reset Game",font = 10,fg ="red",bg = "black",command = reset_game).pack(pady = 20)
root.mainloop()