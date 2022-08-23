from tkinter import *


def convert():
    input = int(entry.get())
    result = input * 1.6
    output.config(text=result)


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=1)

output = Label(text="0")
output.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=convert, width=6)
button.grid(column=1, row=2)


window.mainloop()

