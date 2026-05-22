from tkinter import *
from tkinter.ttk import *

finestra = Tk()

llens = Frame(finestra, padding = 10)
llens.grid()

Label(llens, text="La primera finestra").grid(column=0, row = 0)
Button(llens, text="Sortir", command=finestra.destroy).grid(column = 1, row = 0)

finestra.mainloop()