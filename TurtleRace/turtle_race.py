from turtle import Turtle, Screen
import random

# import tkinter as tk
# from tkinter import ttk

# NORM_FONT= ("Verdana", 10)
# def popupmsg(msg):
#     popup = tk.Tk()
#     popup.wm_title("Achtung, achtung!")
#     label = ttk.Label(popup, text=msg, font=NORM_FONT)
#     label.pack(side="top", fill="x", pady=100)
#     B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
#     B1.pack()
#     popup.mainloop()


is_race_on = True
tim_tin=[]
for i in range(6):
    tim=Turtle()
    tim_tin.append(tim)

screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour:")
print(user_bet)
colors =["red","orange","yellow","green","blue","purple"]
for i in range(6):
    tim_tin[i].shape("turtle")
    tim_tin[i].penup()
    tim_tin[i].goto(x=-230,y=75-i*30)
    tim_tin[i].color(colors[i])

while user_bet and is_race_on:
    for i in range(6):
        random_distance = random.randint(0,10)
        tim_tin[i].forward(random_distance)
        if tim_tin[i].xcor() >= 200:
            is_race_on = False
            winner_turtle=tim_tin[i]
            winner_color=tim_tin[i].pencolor()
            if winner_color == user_bet:
                print(f"The winner is the {winner_color} Turtle! You won! :)")
                #popupmsg(f"The winner is the {winner_color} Turtle! You won! :)")
            else:
                print(f"The winner is the {winner_color} Turtle! Your {user_bet} Turtle didn't win! :(")
               # popupmsg(f"The winner is the {winner_color} Turtle! Your {user_bet} Turtle didn't win! :(")


screen.exitonclick()
