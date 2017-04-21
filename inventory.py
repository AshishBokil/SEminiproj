#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import time
import mysql.connector
from mysql.connector import Error


con=mysql.connector.connect(user='root',password='my123',host='localhost',database='Bills')
c=con.cursor()


def select():
	c.execute("SELECT price from storage where category="+str(var.get()))
	cost=c.fetchone()   
#  array=mysql_fetch_assoc(str(cost))

	c.execute("SELECT name from storage where category="+str(var.get()))
	Name=c.fetchone()

	c.execute("SELECT company from storage where category="+str(var.get()))
	brand=c.fetchone()


	c.execute("SELECT quantity from storage where category="+str(var.get()))
	quantity=c.fetchone()

	treeview.insert('', 'end',  values=(var.get(),Name,brand,1,2,quantity))


     



root =Tk()
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("1200x600")
root.title("Inventory")
var =StringVar(root)
# initial value
var.set('red')
choices = ['None', 'Tshirt', 'shirt', 'jeans','Trousers']
option =OptionMenu(root, var, *choices)
option.grid(row=1, padx=10, pady=10)


button =Button(root, text="check value slected", command=select)
button.grid(row=3, padx=20, pady=10)

#treeview-----------
tree =ttk.Treeview(root, columns=('Category','Item ID','Name', 'Brand','Price','Quantity'))

tree.heading('#0', text='Category')
tree.heading('#1', text='Item ID')
tree.heading('#2', text='Name')
tree.heading('#3', text='Brand')
tree.heading('#4', text='Price')
tree.heading('#5', text='Quantity')
tree.heading('#6')


tree.column('#0', stretch=YES)
tree.column('#1', stretch=YES)
tree.column('#2', stretch=YES)
tree.column('#3', stretch=YES)
tree.column('#4', stretch=YES)
tree.column('#5', stretch=YES)
tree.column('#6',width=0)

tree.grid(row=15, sticky='nsew')
treeview =tree
# Initialize the counter

i = 1



root.mainloop()
