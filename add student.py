import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("500x500")
window.title("Meri App")

def simple():
    import connectdb
    name = entername.get()
    email = enteremail.get()
    RolLNo = enterRollNo.get()
    DateofBirth = enterDateofBirth.get()
    Address = enterAddress.get()
    FatherName = enterFatherName.get()
    MotherName = enterMotherName.get()
    BloodGroup = enterBloodGroup.get()
    Religon = enterReligon.get()
    Caste = enterCaste.get()
    Sibblings = enterSibblings.get()
    ClassTeacher = enterClassTeacher.get()
    
        
    sql = '''insert into student_master(name,email,RollNo,dateofbirth,Address,Fathername,Mothername,BloodGroup,Religon,Caste,Sibblings,ClassTeacher)
 values('  ''' +name+ ''' ',' '''+email+''' ',' '''+RollNo+''' ',' '''+DateofBirth+''' ',' '''+Address+''' ',' '''+FatherName+''' ',' '''+MotherName+''' ',' '''+BloodGroup+''' ',' '''+Religon+''' ',' '''+Caste+''' ',' '''+Sibblings+''' ',' '''+ClassTeacher+''' ')'''
    #print(sql)
    connectdb.mycursor.execute(sql)
    lblres.config(text='inserted '+name)
    #entername.config(text='')
    #print(entername.get(),'i')
	
lblname = Label(window, text="Enter Student Name")
entername = Entry(window)

lblemail = Label(window, text="Enter Student Email")
enteremail = Entry(window)

lblRollNo = Label(window, text="Enter student Roll No")
enterRollNo = Entry(window)

lblDateofBirth = Label(window, text="Enter Student Date of Birth")
enterDateofBirth = Entry(window)

lblAddress = Label(window, text="Enter Address")
enterAddress = Entry(window)

lblFatherName = Label(window, text="Enter FatherName")
enterFatherName = Entry(window)

lblMotherName = Label(window, text="Enter MotherName")
enterMotherName = Entry(window)

lblBloodGroup= Label(window, text="Enter BloodGroup")
enterBloodGroup = Entry(window)

lblReligon = Label(window, text="Enter Religon")
enterReligon = Entry(window)

lblCaste = Label(window, text="Enter Caste")
enterCaste = Entry(window)

lblSibblings = Label(window, text="Enter Sibblings")
enterSibblings = Entry(window)

lblClassTeacher = Label(window, text="Enter ClassTeacher")
enterClassTeacher = Entry(window)


lblresult = Label(window, text='Result')

lblname.grid(column=1,row=1)
entername.grid(column=2,row=1)

lblemail.grid(column=1,row=2)
enteremail.grid(column=2,row=2)

lblRollNo.grid(column=1,row=3)
enterRollNo.grid(column=2,row=3)

lblDateofBirth.grid(column=1,row=4)
enterDateofBirth.grid(column=2,row=4)

lblAddress.grid(column=1,row=5)
enterAddress.grid(column=2,row=5)

lblFatherName.grid(column=1,row=6)
enterFatherName.grid(column=2,row=6)

lblMotherName.grid(column=1,row=7)
enterMotherName.grid(column=2,row=7)

lblBloodGroup.grid(column=1,row=8)
enterBloodGroup.grid(column=2,row=8)

lblReligon.grid(column=1,row=9)
enterReligon.grid(column=2,row=9)

lblCaste.grid(column=1,row=10)
enterCaste.grid(column=2,row=10)

lblSibblings.grid(column=1,row=11)
enterSibblings.grid(column=2,row=11)

lblClassTeacher.grid(column=1,row=12)
enterClassTeacher.grid(column=2,row=12)


btnsub = Button(window, text="Submit", command=simple, bg='blue', fg='white')
btnsub.grid(column=1,row=13)
#enterbtnsub.grid(column=2,row=7)

	
lblres = Label(window, text="...")
lblres.grid(column=1,row=14)
window.mainloop()
