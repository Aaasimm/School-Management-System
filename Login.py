import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("500x500")
window.title("Login")

def register():
    import connectdb
    username = enterusername.get()
    password = enterpassword.get()
    import connectdb
    sqli= "Select * From school_master where username='"+username+"' and password='"+password+"'"
    connectdb.mycursor.execute(sqli)
    print(sqli)
    mytables = connectdb.mycursor.fetchall()
    for i in range(0,len(mytables)):
        print(mytables[i][4])
        if(username==mytables[i][1] and password==mytables[i][2]):
            lblres.config(text='Welcome '+ mytables[i][4])
            print("Welcome")
        else:
            print("sorry")

        
        
        
lblusername = Label(window, text="Enter username")
enterusername = Entry(window)

lblpassword = Label(window, text="Enter Password")
enterpassword = Entry(window)

lblusername.grid(column=1,row=1)
enterusername.grid(column=2,row=1)

lblpassword.grid(column=1,row=2)
enterpassword.grid(column=2,row=2)

btnsub = Button(window, text="Login", command=register, bg='blue', fg='white')
btnsub.grid(column=1,row=4)

lblres = Label(window, text="...")
lblres.grid(column=1,row=5)
window.mainloop()

