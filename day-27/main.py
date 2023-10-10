from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(
    padx=100, pady=100, background="green"
)  # add spaces around the contents(label/button/entry/listbox...)

# label
my_label = Label(text="I'm a label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)


# button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=2, row=0)

# entry
input = Entry(width=30)
input.insert(END, string="Some text to begin with.")
input.grid(column=3, row=2)


window.mainloop()
