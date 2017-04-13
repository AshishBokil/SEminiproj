#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import time


_name_="_main_"
#total=StringVar()
sum=0


class Begueradj(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.parent=parent
        
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        #self.parent.geometry=("1200x800")
        self.parent.title("Canvas Test")       
        self.parent.grid_rowconfigure(0,weight=0)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")
       

        # Define the different GUI widgets
        self.localtime=time.asctime(time.localtime(time.time()))
        self.labelhead=Label(self.parent,font=('arial',30,'bold'),text="A2N Billing system",fg="Blue",bd='0',anchor='w')
        self.labelhead.grid(row=0)


        self.dose_label = Label(self.parent, text = "Item ID:")
        self.dose_entry = Entry(self.parent)
        self.dose_label.grid(row = 1, column = 0, sticky = 'W')
        self.dose_entry.grid(row = 1, column = 1)

        self.modified_label = Label(self.parent, text = "Date Modified:")
        self.labeldate=Label(self.parent,font=('arial',10,'bold'),text=self.localtime,fg="Black",bd='0',anchor='w')
        self.modified_label.grid(row = 2, column = 0, sticky = 'w')
        self.labeldate.grid(row=2,column=1)


        self.submit_button = Button(self.parent, text = "Insert", command = self.insert_data)
        self.submit_button.grid(row = 3, column = 1, sticky = W)
        self.exit_button = Button(self.parent, text = "Exit", command = self.parent.quit)
        self.exit_button.grid(row = 1, column = 3)


        # Set the treeview
        self.tree = ttk.Treeview( self.parent, columns=('Item ID','Price', 'Modification date'))
        self.tree.heading('#0', text='Item NO')
        self.tree.heading('#1', text='Item ID')
        self.tree.heading('#2', text='Price')
        self.tree.heading('#3', text='Modification Date')
        self.tree.column('#0', stretch=YES)
        self.tree.column('#1', stretch=YES)
        self.tree.column('#2', stretch=YES)
        self.tree.column('#3', stretch=YES)
        self.tree.grid(row=15, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.i = 1

#total amount
  #      self.amount_total = Label(self.parent, text = "Total Amount:")
  #      self.amount_ = Entry(self.parent,text=self.total)
   #     self.amount_.grid(column=1)
    #    self.amount_total.grid(column=0)



        self.button_del = Button(self.parent, text="del", command=self.delete)
        self.button_del.grid()
        self.button_payment = Button(self.parent, text="Proceed to Payment", command=self.delete)
        self.button_payment.grid()


    def insert_data(self):
        """
        Insertion method.
        """
        global sum
        self.treeview.insert('', 'end', text="Item_"+str(self.i), values=(self.dose_entry.get()+" mg",(self.i)*100, self.localtime))
        # Increment counter
        sum= sum + ((self.i)*100)
        self.dose_total = Label(self.parent, text = "TOal Amount:"+str(sum))
        self.dose_total.grid(row =20, column = 1, sticky = 'W')

        self.i = self.i + 1

    def delete(self):
        selected_item = self.tree.selection()[0] ## get selected item
        self.treeview.delete(selected_item)









def main():
    root=Tk()
    d=Begueradj(root)
    root.mainloop()

if _name_=="_main_":
    main()
