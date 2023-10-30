# Tkinter : inbuilt python module which is used to create GUI applacation
from tkinter import *

sc = Tk() # screen tkinter store
sc.geometry("600x300") # w x h
sc.title("MY APP")

lbl_var = StringVar()

def mychoice(msg):
    
    lbl_var.set(msg)

# lbl = Label(sc,text="Welcome to Tkinter",font=('arial',26,'bold'))
# lbl.place(x=10,y=10)

btn1 = Button(sc,text="ROCK",font=('arial',26,'bold'),activebackground="blue",activeforeground="White",command=lambda :mychoice("ROCK"))
btn1.place(x=10,y=10)

btn2 = Button(sc,text="PAPER",font=('arial',26,'bold'),activebackground="blue",activeforeground="White",command=lambda :mychoice("PAPER"))
btn2.place(x=160,y=10)

btn3 = Button(sc,text="SCISSOR",font=('arial',26,'bold'),activebackground="blue",activeforeground="White",command=lambda :mychoice("SCISSOR"))
btn3.place(x=340,y=10)

lbl = Label(sc,textvariable=lbl_var,font=('arial',26,'bold'))
lbl.place(x=10,y=120)



sc.mainloop()