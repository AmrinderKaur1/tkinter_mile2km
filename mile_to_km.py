from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(height=300, width=400)
window.config(padx=50, pady=50)


def calculation():
    new_t = int(entry.get()) * 1.6
    cal.config(text=new_t)


# entry
entry = Entry(text="Enter here.")
entry.grid(row=0, column=1)

# label
my_label = Label(text="Miles")
my_label.grid(row=0, column=2)
my_label2 = Label(text="is equal to")
my_label2.grid(row=1, column=0)
my_label3 = Label(text="km")
my_label3.grid(row=1, column=2)
cal = Label(text="0")
cal.grid(row=1, column=1)

# Button
button = Button(text="Calculate", command=calculation)
button.grid(row=2, column=1)

# exit screen
window.mainloop()
