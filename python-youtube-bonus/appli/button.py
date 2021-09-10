from tkinter import *

def click():
    print("You click the button")

window = Tk()

button = Button(window,
                text ="click me!",
                command=click,
                font=('Times New Roman',30),
                fg= "black",
                bg= "pink",
                activeforeground='orange',
                activebackground='black')

button.pack()

window.mainloop()