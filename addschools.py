import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("500x500")
window.title("Meri App")

def simple():
    import connectdb
    name = entername.get()
    email = enteremail.get()
    phone = enterphone.get()
    board = enterboard.get()
    city = entercity.get()
    pincode = enterpincode.get()    
    sql = '''insert into school_master(name,email,phone,board,city,pincode)
 values('  ''' +name+ ''' ',' '''+email+''' ',' '''+phone+''' ',' '''+board+''' ',' '''+city+''' ',' '''+pincode+''' ')'''
    #print(sql)
    connectdb.mycursor.execute(sql)
    lblres.config(text='inserted '+name)
    #entername.config(text='')
    #print(entername.get(),'i')
	
lblschool = Label(window, text="Enter School Name")
entername = Entry(window)

lblemail = Label(window, text="Enter School Email")
enteremail = Entry(window)

lblphone = Label(window, text="Enter School Phone")
enterphone = Entry(window)

lblboard = Label(window, text="Enter School board")
enterboard = Entry(window)

lblcity = Label(window, text="Enter School City")
entercity = Entry(window)

lblpincode = Label(window, text="Enter School Pincode")
enterpincode = Entry(window)


lblresult = Label(window, text='Result')

lblschool.grid(column=1,row=1)
entername.grid(column=2,row=1)

lblemail.grid(column=1,row=2)
enteremail.grid(column=2,row=2)

lblphone.grid(column=1,row=3)
enterphone.grid(column=2,row=3)

lblboard.grid(column=1,row=4)
enterboard.grid(column=2,row=4)

lblcity.grid(column=1,row=5)
entercity.grid(column=2,row=5)

lblpincode.grid(column=1,row=6)
enterpincode.grid(column=2,row=6)

btnsub = Button(window, text="Submit", command=simple, bg='blue', fg='white')
btnsub.grid(column=1,row=7)
#enterbtnsub.grid(column=2,row=7)

	
lblres = Label(window, text="...")
lblres.grid(column=1,row=9)
window.mainloop()





