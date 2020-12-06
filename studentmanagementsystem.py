def addstudent():
    def submitadd():
        id=idval.get()
        name=nameval.get()
        email=emailval.get()
        mobnum=mobval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%m/%d/%Y")
        try:
            strr='insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,email,mobnum,address,gender,dob,addedtime,addeddate))
            con.commit()
            res=messagebox.askyesnocancel('Success','ID{} Name{} Added Successfully. Do you want to clear the data?'.format(id,name),parent=addroot)
            if(res==TRUE):
                idval.set('')
                nameval.set('')
                emailval.set('')
                mobval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Error','ID already exist. Try Different ID',parent=addroot)
        strr='select * from studentdata1'
        mycursor.execute(strr)
        datastud = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datastud:
            valdata=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=valdata)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Add Student')
    addroot.config(bg='Gold')
    addroot.iconbitmap('student.ico.ico')
    addroot.resizable(FALSE,FALSE)
    # --------------------------------Add Student Labels---------------------------#
    idlabel = Label(addroot, text='Student ID: ', bg='black',fg='gold',font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Name: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    emaillabel = Label(addroot, text='Email: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=130)

    mobilelabel = Label(addroot, text='Mobile Number: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Address: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Gender: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Date of Birth: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)
    #----------------------------------------------------Add Student Entry--------------------------------------#
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    mobval= StringVar()
    addressval= StringVar()
    genderval= StringVar()
    dobval= StringVar()

    identry = Entry(addroot,font=('times',15,'bold'),bd=5,bg='black',fg='gold',textvariable=idval,insertbackground = 'gold')
    identry.place(x=250,y=10)
    nameentry = Entry(addroot, font=('times', 15, 'bold'), bd=5,bg='black',fg='gold', textvariable=nameval,insertbackground = 'gold')
    nameentry.place(x=250, y=70)
    emailentry = Entry(addroot, font=('times', 15, 'bold'), bd=5,bg='black',fg='gold', textvariable=emailval,insertbackground = 'gold')
    emailentry.place(x=250, y=130)
    mobentry = Entry(addroot, font=('times', 15, 'bold'), bd=5,bg='black',fg='gold', textvariable=mobval,insertbackground = 'gold')
    mobentry.place(x=250, y=190)
    addressentry = Entry(addroot, font=('times', 15, 'bold'), bd=5,bg='black',fg='gold', textvariable=addressval,insertbackground = 'gold')
    addressentry.place(x=250, y=250)
    genderentry = Entry(addroot, font=('times', 15, 'bold'), bd=5,bg='black',fg='gold', textvariable=genderval,insertbackground = 'gold')
    genderentry.place(x=250, y=310)
    dobentry = Entry(addroot, font=('times', 15, 'bold'), bd=5,bg='black',fg='gold', textvariable=dobval,insertbackground = 'gold')
    dobentry.place(x=250, y=370)

    #--------------------------------------submit Button-----------------------------------#
    submitbtn = Button(addroot,text = 'Submit', font = ('times',15,'bold'),width=20,bd=5,activebackground='gold',bg='black',fg='gold', command = submitadd)
    submitbtn.place(x=120,y=420)

    addroot.mainloop()

def searchstudent():
    def searchstud():
        id = idval.get()
        name = nameval.get()
        email = emailval.get()
        mobnum = mobval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%m/%d/%Y")
        if (id!=''):
            strr='select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datastud = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datastud:
                valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=valdata)
        elif (name!=''):
            strr='select * from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datastud = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datastud:
                valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=valdata)
        elif (email!=''):
            strr='select * from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datastud = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datastud:
                valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=valdata)
        elif (mobnum!=''):
            strr='select * from studentdata1 where mobnum =%s'
            mycursor.execute(strr,(mobnum))
            datastud = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datastud:
                valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=valdata)

        elif (address!=''):
            strr='select * from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datastud = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datastud:
                valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=valdata)
        elif (gender!=''):
            strr='select * from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datastud = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datastud:
                valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=valdata)
        elif (dob!=''):
            strr='select * from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datastud = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datastud:
                valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=valdata)
        elif (addeddate!=''):
            strr='select * from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datastud = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datastud:
                valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=valdata)


    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('500x540+220+200')
    searchroot.title('Search Student')
    searchroot.config(bg='Gold')
    searchroot.iconbitmap('student.ico.ico')
    searchroot.resizable(FALSE, FALSE)
    # --------------------------------search Student Labels---------------------------#
    idlabel = Label(searchroot, text='Student ID: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Name: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    emaillabel = Label(searchroot, text='Email: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=130)

    mobilelabel = Label(searchroot, text='Mobile Number: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                            relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Address: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                             relief=GROOVE,
                             borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Gender: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Date of Birth: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                         relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)
    datelabel = Label(searchroot, text='Date: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                     relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)
        # ----------------------------------------------------search Student Entry--------------------------------------#
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    mobval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=idval,
                        insertbackground='gold')
    identry.place(x=250, y=10)
    nameentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=nameval,
                          insertbackground='gold')
    nameentry.place(x=250, y=70)
    emailentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=emailval,
                           insertbackground='gold')
    emailentry.place(x=250, y=130)
    mobentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=mobval,
                         insertbackground='gold')
    mobentry.place(x=250, y=190)
    addressentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=addressval,
                             insertbackground='gold')
    addressentry.place(x=250, y=250)
    genderentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=genderval,
                            insertbackground='gold')
    genderentry.place(x=250, y=310)
    dobentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=dobval,
                         insertbackground='gold')
    dobentry.place(x=250, y=370)
    dateentry = Entry(searchroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=dateval,
                     insertbackground='gold')
    dateentry.place(x=250, y=430)

        # --------------------------------------search Button-----------------------------------#
    srchbtn = Button(searchroot, text='Search', font=('times', 15, 'bold'), width=20, bd=5, activebackground='gold',
                           bg='black', fg='gold', command=searchstud)
    srchbtn.place(x=120, y=480)

    searchroot.mainloop()
    print('Searching student')

def deletestudent():
    cc = studenttable.focus()
    content=studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Deleted','ID {} has been deleted successfully.'.format(pp))
    strr='select * from studentdata1'
    mycursor.execute(strr)
    datastud = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datastud:
        valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=valdata)

def updatestudent():
    def updatestud():
        id=idval.get()
        name=nameval.get()
        email=emailval.get()
        mobnum=mobval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        date=dateval.get()
        time=timeval.get()

        strr='update studentdata1 set name=%s,email=%s,mobnum=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,email,mobnum,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Updated','ID{} Data has been updated successfully.'.format(id),parent=updateroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datastud = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datastud:
            valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=valdata)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('500x600+220+160')
    updateroot.title('Update Student')
    updateroot.config(bg='Gold')
    updateroot.iconbitmap('student.ico.ico')
    updateroot.resizable(FALSE, FALSE)
        # --------------------------------search Student Labels---------------------------#
    idlabel = Label(updateroot, text='Student ID: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                        relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Name: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    emaillabel = Label(updateroot, text='Email: ', bg='black', fg='gold', font=('times', 20, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=130)

    mobilelabel = Label(updateroot, text='Mobile Number: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                            relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Address: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                             relief=GROOVE,
                             borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Gender: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                            relief=GROOVE,
                            borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Date of Birth: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                         relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)
    datelabel = Label(updateroot, text='Date: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                          relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)
    timelabel = Label(updateroot, text='Time: ', bg='black', fg='gold', font=('times', 20, 'bold'),
                      relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)
        # ----------------------------------------------------search Student Entry--------------------------------------#
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    mobval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=idval,
                        insertbackground='gold')
    identry.place(x=250, y=10)
    nameentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=nameval,
                          insertbackground='gold')
    nameentry.place(x=250, y=70)
    emailentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=emailval,
                           insertbackground='gold')
    emailentry.place(x=250, y=130)
    mobentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=mobval,
                         insertbackground='gold')
    mobentry.place(x=250, y=190)
    addressentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold',
                             textvariable=addressval,
                             insertbackground='gold')
    addressentry.place(x=250, y=250)
    genderentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=genderval,
                            insertbackground='gold')
    genderentry.place(x=250, y=310)
    dobentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=dobval,
                         insertbackground='gold')
    dobentry.place(x=250, y=370)
    dateentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=dateval,
                          insertbackground='gold')
    dateentry.place(x=250, y=430)
    timeentry = Entry(updateroot, font=('times', 15, 'bold'), bd=5, bg='black', fg='gold', textvariable=timeval,
                      insertbackground='gold')
    timeentry.place(x=250, y=490)

        # --------------------------------------search Button-----------------------------------#
    updtbtn = Button(updateroot, text='Update', font=('times', 15, 'bold'), width=20, bd=5, activebackground='gold',
                         bg='black', fg='gold', command=updatestud)
    updtbtn.place(x=120, y=550)
    cc = studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if(len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        emailval.set(pp[2])
        mobval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
    print('Student is updated')
def showallstudents():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datastud = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datastud:
        valdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=valdata)
def export():
    ps=filedialog.asksaveasfilename()
    aa=studenttable.get_children()
    id,name,email,mobnum,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in aa:
        content=studenttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),email.append(pp[2]),mobnum.append(pp[3]),
        address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['ID','Name','Email','Mobile Number','Address','Gender','D.O.B','Date','Time']
    df=pandas.DataFrame(list(zip(id,name,email,mobnum,address,gender,dob,addeddate,addedtime)),columns=dd)
    path= r'{}.csv'.format(ps)
    df.to_csv(path,index=FALSE)
    messagebox.showinfo('Save File', 'File has been saved'.format(path))
def exit():
    res = messagebox.askyesnocancel('Exit','Are you sure you want to exit this window?')
    if(res==TRUE):
        root.destroy()
####################################Connection of Database###################################
def Connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Wrong ID or Password. Please try again.',parent=dbroot)
            return
        try:
            strr='create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            strr='create table studentdata1(id int,name varchar(20),email varchar(30),mobnum varchar(15),address varchar(100), gender varchar(10),dob varchar(20),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Success', 'Database has been connected', parent=dbroot)

        except:
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Success','Database has been connected',parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.iconbitmap('student.ico.ico')
    dbroot.resizable(FALSE,FALSE)
    dbroot.title("Database Connection")
    dbroot.config(bg='gold')
    dbroot.geometry('470x250+800+230')
    #--------------------------------------ConnectDBLabel---------------------------------#
    hostLabel = Label(dbroot,text='Enter Host: ', bg = 'black',fg='gold', font=('times',20,'bold'), relief=GROOVE,borderwidth = 3,width=12, anchor ='w')
    hostLabel.place(x=10,y=10)

    userLabel = Label(dbroot, text='Enter User: ', bg='black',fg='gold', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    userLabel.place(x=10, y=80)

    passwordLabel = Label(dbroot, text='Enter Password: ', bg='black',fg='gold', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    passwordLabel.place(x=10, y=160)

    #---------------------------------------ConnectDBEntry-------------------------------#
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostEntry = Entry(dbroot,font=('times',15,'bold'),bd=5,bg='black',fg='gold',insertbackground='gold',text = hostval)
    hostEntry.place(x=250,y=10)

    userEntry = Entry(dbroot, font=('times', 15, 'bold'), bd=5, bg='black',fg='gold',insertbackground='gold', text=userval)
    userEntry.place(x=250, y=80)

    passwordEntry = Entry(dbroot, font=('times', 15, 'bold'), bd=5, bg='black',fg='gold',insertbackground='gold', text=passwordval)
    passwordEntry.place(x=250, y=160)

    #--------------------------------------ConnectDBButton---------------------------------#
    submitbutton = Button(dbroot, text='Submit', font=('times',15,'bold'),width=20,bg='black',fg='gold',activebackground='gold',command=submitdb)
    submitbutton.place(x=150,y=205)

    dbroot.mainloop()
#############################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    date_string = time.strftime('%d:%m:%Y')
    clock.config(text='Date: '+date_string+"\n"+"Time: "+time_string, fg = 'gold')
    clock.after(200,tick)
########################################### INTRO SLIDER ###################################################
def IntroLabelTick():
    global count,text
    if (count>=len(ss)):
        count=0
        text=''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(200,IntroLabelTick)

#########################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('Student Management System')
root.config(bg='black')
root.geometry('1174x700+200+50')
root.iconbitmap('student.ico.ico')
root.resizable(FALSE,FALSE)
############################################  Frames ##################################
#-------------------------------------------Data Entry Frame -------------------------#
DataEntryFrame = Frame(root,bg='black',relief=GROOVE, borderwidth = 5)
DataEntryFrame.place(x=10,y=80, width=500,height = 600)
frontlabel = Label(DataEntryFrame,text = '------------WELCOME-------------',width=30, font=('times',22,'bold'),bg='gold')
frontlabel.pack(side=TOP,expand = TRUE)

addbtn = Button(DataEntryFrame,text='Add Student',width=25,font=('times',20,'bold'),bd=6,bg='black',fg='gold',activebackground='gold',relief=RIDGE,command = addstudent)
addbtn.pack(side=TOP,expand=TRUE)

searchbtn = Button(DataEntryFrame,text='Search Student',width=25,font=('times',20,'bold'),bd=6,bg='black',fg='gold',activebackground='gold',relief=RIDGE,command=searchstudent)
searchbtn.pack(side=TOP,expand=TRUE)

deletebtn = Button(DataEntryFrame,text='Delete Student',width=25,font=('times',20,'bold'),bd=6,bg='black',fg='gold',activebackground='gold',relief=RIDGE,command =deletestudent)
deletebtn.pack(side=TOP,expand=TRUE)

updatebtn = Button(DataEntryFrame,text='Update Student',width=25,font=('times',20,'bold'),bd=6,bg='black',fg='gold',activebackground='gold',relief=RIDGE, command = updatestudent)
updatebtn.pack(side=TOP,expand=TRUE)

showallbtn = Button(DataEntryFrame,text='Show All Students',width=25,font=('times',20,'bold'),bd=6,bg='black',fg='gold',activebackground='gold',relief=RIDGE,command = showallstudents)
showallbtn.pack(side=TOP,expand=TRUE)

exportbtn = Button(DataEntryFrame,text='Export Data',width=25,font=('times',20,'bold'),bd=6,bg='black',fg='gold',activebackground='gold',relief=RIDGE,command =export)
exportbtn.pack(side=TOP,expand=TRUE)

exitbtn = Button(DataEntryFrame,text='Exit',width=25,font=('times',20,'bold'),bd=6,bg='black',fg='gold',activebackground='gold',relief=RIDGE,command = exit)
exitbtn.pack(side=TOP,expand=TRUE)
#-------------------------------------------Show Data Frame -------------------------#
ShowDataFrame = Frame(root,bg='black',relief=GROOVE, borderwidth = 5)
ShowDataFrame.place(x=550,y=80, width=620,height = 600)
#------------------------------------------------------------------------------------#
style = ttk.Style()
style.configure('Treeview.Heading',font=('times',20,'bold'),foreground='gold')
style.configure('Treeview',font=('times',15,'bold'),background='gold',foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient = HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient = VERTICAL)
studenttable = Treeview(ShowDataFrame,column=('ID','Name','Email','Mobile Number','Address','Gender','D.O.B','Date','Time'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Email',text='Email')
studenttable.heading('Mobile Number',text='Mobile Number')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Date',text='Date')
studenttable.heading('Time',text='Time')
studenttable['show']='headings'
studenttable.column('ID',width=100)
studenttable.column('Name',width=200)
studenttable.column('Email',width=300)
studenttable.column('Mobile Number',width=100)
studenttable.column('Address',width=300)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Date',width=150)
studenttable.column('Time',width=150)
studenttable.pack(fill = BOTH,expand=1)


#######################################################################################
ss = 'Student Management System'
count = 0
text = ''
############################################  Slider ###################################
SliderLabel = Label(root,text=ss, font=('times new roman',25,'bold'),relief = RIDGE, borderwidth=5,width=32,bg='Red')
SliderLabel.place(x=240,y=0)
IntroLabelTick()
############################################  Clock ###################################
clock = Label(root,font=('times new roman',14,'bold'),relief = RIDGE, borderwidth=5,bg='black')
clock.place(x=0,y=0)
tick()
############################################ ConnectDatabaseButton ###################################
connectbutton = Button(root,text='Connect To Database',font=('times new roman',15,'bold'),relief = RIDGE,borderwidth=6,width=21,bg='black',fg='gold',
                       activebackground='gold', command=Connectdb)
connectbutton.place(x=930,y=0)

root.mainloop()
