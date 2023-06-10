import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("500x500")
window.title("Registration")

def register():
    if (password.get()==passwordagain.get()):
        import connectdb
        username = username.get()
        password = password.get()
        passwordagain = passwordagain.get()
        Role = Role.get()
        sql = '''insert into theusers(username,password,Role,)
        values('  ''' +username+ ''' ',' '''+password+''' ',' '''+Role+''' ')'''
        connectdb.mycursor.execute(sql)

lblusername = Label(window, text="Enter username")
enterusername = Entry(window)

lblpassword = Label(window, text="Enter password")
enterpassword = Entry(window)

lblpasswordagain = Label(window, text="Enter password again")
enterpasswordagain = Entry(window)

lblusername.grid(column=1,row=1)
enterusername.grid(column=2,row=1)

lblpassword.grid(column=1,row=2)
enterpassword.grid(column=2,row=2)

lblpasswordagain.grid(column=1,row=3)
enterpasswordagain.grid(column=2,row=3)

btnsub = Button(window, text="Submit", command=register, bg='blue', fg='white')
btnsub.grid(column=1,row=4)

lblres = Label(window, text="...")
lblres.grid(column=1,row=5)
window.mainloop()