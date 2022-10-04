import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def flip_cards():
    canvas.itemconfig(image_on_top, image=back_card)
    canvas.itemconfig(title_on_top, text="English", fill="white")
    canvas.itemconfig(text_on_top, text=current_card["English"], fill="white")


def known():
    french_list.remove(current_card)
    words_to_learn = pandas.DataFrame(french_list)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_word()


def next_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(french_list)
    canvas.itemconfig(text_on_top, text=current_card["French"], fill="black")
    canvas.itemconfig(title_on_top, text="French", fill="Black")
    canvas.itemconfig(image_on_top, image=front_card)
    timer = window.after(3000, func=flip_cards)

window = Tk()
window.title("Flashy 📸")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_cards)


# Getting data from csv
try:
    french_df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    french_df = pandas.read_csv("./data/french_words.csv")
    french_list = french_df.to_dict(orient="records")
else:
    french_list = french_df.to_dict(orient="records")

canvas = Canvas(highlightthickness=0, width=800, height=526, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
image_on_top = canvas.create_image(400, 263, image=front_card)
title_on_top = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
text_on_top = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

right_button = Button(image=right, highlightthickness=0, command=known)
right_button.config(padx=50)
right_button.grid(row=2, column=2)

wrong_button = Button(image=wrong, highlightthickness=0, command=next_word)
wrong_button.config(padx=50)
wrong_button.grid(row=2, column=1)

next_word()
window.mainloop()
