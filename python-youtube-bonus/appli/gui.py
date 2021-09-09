from tkinter import *
from PIL import *
import os

#widgets = GUI elements: buttons, textboxes, label,images
#window = servers as a container to hold or contain these widgets
script_dir = os.path.dirname(__file__) 
window = Tk() #instantiate a instance of a window
window.geometry("420x420") 
window.title("Gia bao ne")


window.config(background="pink")

window.mainloop() #place window on computer screen, listen for events
