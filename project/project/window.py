from tkinter import *
def create_window():
    new_window = Tk() #Toplevel
    window.destroy()

window = Tk()

Button(window,text = 'create new window',command=create_window).pack()

window.mainloop()