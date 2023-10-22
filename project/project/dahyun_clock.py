'''dahyun+darwin = dahwin'''
from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    day_string = strftime("%B %d , %Y")
    day_label.config(text=day_string)
    dahyun.after(1000, update)


dahyun = Tk()
time_label= Label(dahyun,font=('Arial',50),fg='#FF0000',bg='black')
time_label.pack()
day_label= Label(dahyun,font=('BOLD',20))
day_label.pack()
date_label= Label(dahyun,font=('BOLD',50))
date_label.pack()
update()
dahyun.mainloop()

# with outgui

# from time import *
#
# def update():
#     time_string = strftime("%I:%M:%S %p")
#     print(time_string)
#     day_string = strftime("%A")
#     print(day_string)
#     day_string = strftime("%B %d , %Y")
#     print(day_string)
#     sleep(1)
#     update()
#
# update()
