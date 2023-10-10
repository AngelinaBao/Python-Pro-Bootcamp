from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pd.read_csv("data/to_learn_words.csv") # return DataFrame or TextFileReader
except FileNotFoundError:
    original_data = pd.read_csv("data/English_Chinese_Words.csv") 
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records") # ‘records’ : list like [{column -> value}, … , {column -> value}]


def next_word():
    global current_card, flip_timer

    root.after_cancel(flip_timer)
    current_card = choice(word_dict)
    canvas.itemconfig(word_category, text="English", fill="black")
    canvas.itemconfig(word_content, text=current_card["English"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    root.after(3000, func=flip_card)

def flip_card():   
    global current_card
    canvas.itemconfig(word_category, text="Chinese", fill="white")
    canvas.itemconfig(word_content, text=current_card["Chinese"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)

def remove_word():
    next_word()
    word_dict.remove(current_card)
    # print(f"unknown words length: {len(word_dict)}")
    pd.DataFrame(word_dict).to_csv("data/to_learn_words.csv", index=False)

root = Tk()
root.title("IELTS Vocabulary") # window title
root.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = root.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png") #file=... is very important, becuase if we don't specify it, then the first positional argument is the name given to the image
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
word_category = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_content = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_word)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=remove_word)
known_button.grid(column=1, row=1)

next_word()



root.mainloop()

