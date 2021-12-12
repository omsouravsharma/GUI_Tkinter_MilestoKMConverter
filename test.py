# Tkinter GUI
from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text='I am label', font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

new_button = Button(text='New Button')
new_button.grid(row=0, column=2)

def button_click():
    my_label["text"] = "Got Clicked"
    input_text = input.get()
    my_label.config(text=input_text)


button = Button(text='Click Me', command=button_click)
button.grid(row=1, column=1)

input = Entry(width=10)
input.grid(row=2, column=3)
input.get()













window.mainloop()

