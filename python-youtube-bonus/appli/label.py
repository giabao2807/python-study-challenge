
from tkinter import *
from typing import Counter

window = Tk()
#set background for app
window.geometry("420x420")
window.title("Giabaone")
window.config(background="pink")


#label
label = Label(window,
                text="Luv myself everyday",
                font=("Times New Roman",40,'bold'),
                fg="blue",
                bg="black")
label.pack()
#label.pack() center

window.mainloop()