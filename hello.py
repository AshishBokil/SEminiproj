#!/usr/bin/python3

from tkinter import *
import time


root=Tk()
root.geometry("1300x700+0+0")
root.title("A2N Bills")

topframe=Frame(root)
topframe.pack()

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

localtime=time.asctime(time.localtime(time.time()))

labelhead=Label(topframe,font=('arial',30,'bold'),text="A2N Billing system",fg="Blue",bd=10,anchor='w')
labelhead.grid(row=0,column=0)

labeltime=Label(topframe,font=('arial',10,'bold'),text=localtime,fg="Black",bd=10,anchor='w')
labeltime.grid(row=1,column=0)

label1=Label(root,text="Enter ID : ",bg="white",fg="black")
label1.pack()

button1=Button(root,text="Add",fg="Black")
button2=Button(root,text="Reset",fg="Black")

button1.pack()
button2.pack()

root.mainloop()
