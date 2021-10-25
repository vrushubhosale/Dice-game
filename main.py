from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("DICE GAME")
root.geometry("600x400")
root.configure(background = "yellow")

img = ImageTk.PhotoImage(Image.open("dice.jpg"))

player1 = Label(root, text="Player 1", bg= "royal blue", fg= "white")
player1.place(relx = 0.1, rely = 0.3 , anchor= CENTER )

player2 = Label(root, text="Player 2", bg= "royal blue", fg= "white")
player2.place(relx = 0.9, rely = 0.3 , anchor= CENTER )

player_1_score_l = Label(root , bg = "royal blue", fg = "white")
player_1_score_l.place(relx = 0.1, rely = 0.4, anchor= CENTER)

player_2_score_l = Label(root , bg = "royal blue", fg = "white")
player_2_score_l.place(relx = 0.9, rely = 0.4, anchor= CENTER)

random_d_label = Label(root,bg = "chocolate", fg = "white")
random_d_label.place(relx = 0.5, rely = 0.5 , anchor= CENTER)

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(1,6)
    random_d_label["text"] = "PLAYER 1 DICE RANDOM NUMBER"
    player1_score = player1_score + random_no
    player_1_score_l["text"] = str( player1_score)

player1_btn = Button(root, image = img, command = player1)
player1_btn.place(relx = 0.1, rely = 0.6, anchor= CENTER)


player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(1,6)
    random_d_label["text"] = "PLAYER 2 DICE RANDOM NUMBER"
    player2_score = player2_score + random_no2
    player_2_score_l["text"] = str( player2_score)

player2_btn = Button(root, image = img, command = player2)
player2_btn.place(relx = 0.9, rely = 0.6, anchor= CENTER)

root.mainloop()