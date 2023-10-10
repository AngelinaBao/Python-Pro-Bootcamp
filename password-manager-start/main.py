from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "_", "@" "*", "+"]

    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    # insert the generated password to password_entry
    password_entry.insert(0, f"{password}")
    # copy the password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    user = user_entry.get()
    password_text = password_entry.get()
    new_data = {website: {"email": user, "password": password_text}}

    # check if any blank field
    if len(website) == 0 or len(password_text) == 0:
        messagebox.showinfo(
            title="Gentle Reminder", message="Please don't leave any field empty!"
        )
    else:
        try:
            with open("password_file.json", "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            with open("password_file.json", "w") as save_file:
                json.dump(new_data, save_file, indent=4)
        else:
            data.update(new_data)
            with open("password_file.json", "w") as save_file:
                json.dump(data, save_file, indent=4)
        finally:
            web_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- Search Password ------------------------------- #
def search_password():
    search_web = web_entry.get()
    try:
        with open("password_file.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(
                title=search_web,
                message=f"Email: {data[search_web]['email']}\nPassword: {data[search_web]['password']}",
            )
    except KeyError as message:
        messagebox.showinfo(
            title="Oops", message=f"The website {message} doesn't exist in data."
        )
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found.")
    else:
        pyperclip.copy(data[search_web]["password"])
    finally:
        web_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
"""
canvas docs: https://tkdocs.com/tutorial/canvas.html
"""
# create canvas
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# website
web_label = Label(text="Website:", font=("Arial", 10, "normal"))
web_label.grid(column=0, row=1)

webname = StringVar()
web_entry = Entry(width=21, textvariable=webname)
web_entry.focus()  # cursor in the website entry
web_entry.grid(row=1, column=1, sticky="ew")

web_button = Button(text="Search", borderwidth=1, command=search_password)
web_button.grid(row=1, column=2, sticky="ew")

# username
user_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
user_label.grid(column=0, row=2)

username = StringVar()
user_entry = Entry(width=35, textvariable=username)
user_entry.insert(0, "Angelina.Bao@wdc.com")
user_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

# password
password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)

password = StringVar()
password_entry = Entry(width=21, textvariable=password)
password_entry.grid(row=3, column=1, sticky="ew")

password_button = Button(
    text="Generate Password", borderwidth=1, command=generate_password
)
password_button.grid(row=3, column=2, sticky="ew")

# add button
add_button = Button(text="Add", width=36, borderwidth=1, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


root.mainloop()
