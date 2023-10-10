from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=100, height=80)
window.config(padx=30, pady=30, background="lightblue")

# labels
mile_label = Label(text="Miles", font=("Arial", 11, "normal"), background="lightblue")
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 11, "normal"), background="lightblue")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

equal_label = Label(
    text="is equal to", font=("Arial", 11, "normal"), background="lightblue"
)
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

km_num_label = Label(text="0", font=("Arial", 11, "normal"), background="lightblue")
km_num_label.grid(column=1, row=1)


# button
def button_command():
    km = round(float(input.get()) * (1.60934))
    km_num_label.config(text=f"{km}")


button = Button(text="Calculate", command=button_command)
button.grid(column=1, row=2)

# entry
input = Entry(width=9, borderwidth=1)
input.grid(column=1, row=0)

window.mainloop()
