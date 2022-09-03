# Clock program

import tkinter
import time


def update():
    time_sting = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_sting)
    # print(time_sting)

    day_string = time.strftime("%A")
    day_label.config(text=day_string)

    date_string = time.strftime("%d %B %Y")
    date_label.config(text=date_string)

    window.after(ms=1000, func=update)


window = tkinter.Tk()
window.title(string="Clock Program")
window.resizable(width=0, height=0)
window.config(bg="black")

time_label = tkinter.Label(master=window,
                           font=("Times new roman", 80, "italic"),
                           fg="Green", bg="Black")

time_label.pack()

day_label = tkinter.Label(master=window,
                          font=("Times new roman", 60, "bold"),
                          fg="white", bg="black")
day_label.pack()

date_label = tkinter.Label(master=window,
                           font=("Times new roman", 60, "bold"),
                           fg="white", bg="black")
date_label.pack()

update()

window.mainloop()
