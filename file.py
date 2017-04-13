#!/usr/bin/python3

from tkinter import *
#import hello
import os
 
creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
str="Please Login \n" 

  
 
def Login(str):
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
 
    intruction = Label(rootA, text=str) # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
 
   
    rootA.mainloop()

def CheckLogin():
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        rootA.destroy()
        Loggedin()


    else:
      rootA.destroy()
      str="Invalid Credentials Please Try Again \n"
      Login(str)
#   hello.py 


def Loggedin():

   import t3 
	
if os.path.isfile(creds):
    Login(str)
#else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
  #  Signup()
