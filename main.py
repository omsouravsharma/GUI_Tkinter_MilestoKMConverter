# Miles to KM program
from tkinter import *

window = Tk()
window.minsize(width=300, height=200)
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

user_input = Entry(text=0)
user_input.grid(row=2, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=2, column=2)

label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(row=3, column=0)

label_km = Label(text="Km")
label_km.grid(row=3, column=2)

label_answer = Label()
label_answer.grid(row=3, column=1)


def calculate():
    input_value = float(user_input.get())
    label_answer.config(text=round((input_value*1.609),2))


button = Button(text="Calculate", command=calculate)
button.grid(row=4, column=1)


window.mainloop()
