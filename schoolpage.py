import sys
import os
import tkinter
from tkinter import *

window=Tk()

window.title("Running python script")
window.geometry("500x500")

def addschools():
    os.system('addschools.py')
  
def addteachers():
    os.system('addteachers.py')
    
btn = Button(window, text="create schools",
bg="black", fg="white" ,command=addschools)
btn.grid(column=0, row=0)

btn = Button(window, text="create teachers",
bg="black", fg="white" ,command=addteachers)
btn.grid(column=2, row=0)
window.mainloop()
