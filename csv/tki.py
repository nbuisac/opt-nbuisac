from tkinter import *
from tkinter.ttk import *

finestra = Tk()

llens = Frame(finestra, padding = 10)
llens.grid()

l1 = Label(llens, text="La primera finestra")
l1.grid(column=0, row = 0)
b1 = Button(llens, text="Sortir", command=finestra.destroy)
b1.grid(column = 1, row = 0)
## segona part
l1["text"] = "Nou missatge"
b1["text"] = "Apreta'm"
## tercera part
l1.configure(text="Segon missatge")
b1.configure(text="Prem per sortir")