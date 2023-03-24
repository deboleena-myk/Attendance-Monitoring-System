from tkinter import *
w=Tk()
w.geometry('1000x1000')
w.config(background='steelblue')
w.title('Attendance Monitoring System')
img=PhotoImage(file='C:\\Users\\user\\OneDrive\\Documents\\python project\\Tkinter\\icons\\images.png')
w.iconphoto(False, img)
import sqlite3
try:
   db=sqlite3.connect('library_attendance.db')
   cr=db.cursor()
   cr.execute('create table login(name text, registration integer, date date, status boolean)')
   db.commit()
except:
    print('Database created successfully')

#Global variable to store data from the form
x=StringVar()#name
y=StringVar()#registration
u=StringVar()#date
v=StringVar()#status

l1=Label(w,text='Attendance Form',font=('times new roman',25),fg='white',bg='black')
l1.pack()

l2=Label(w,text='Name:',font=('times new roman',22,'bold'),bg='steelblue',fg='white')
l2.place(x=30,y=120)

l3=Label(w,text='Registration:',font=('times new roman',22,'bold'),bg='steelblue',fg='white')
l3.place(x=30,y=160)

l4=Label(w,text='Date:',font=('times new roman',22,'bold'),bg='steelblue',fg='white')
l4.place(x=30,y=200)

l5=Label(w,text='Status:',font=('times new roman',22,'bold'),bg='steelblue',fg='white')
l5.place(x=30,y=240)

#entry box:-
e1=Entry(w,font=('times new roman',22,'bold'))
e1.place(x=200,y=120)

e2=Entry(w,font=('times new roman',22,'bold'))
e2.place(x=200,y=160)

e3=Entry(w,font=('times new roman',22,'bold'))
e3.place(x=200,y=200)

e4=Entry(w,font=('times new roman',22,'bold'))
e4.place(x=200,y=240)

#button
def submit():
    a=x.get()
    b=y.get()
    c=u.get()
    d=v.get()
    cr.execute("insert into login(name, registration, date, status)values(?,?,?,?)",(a,b,c,d))
    db.commit()
b1=Button(w,text='Submit',font=('times new roman',15,'bold'),fg='white',bg='green',command=submit)
b1.place(x=150,y=300)

#clear
def clear():
    x.set('')
    y.set('')
    u.set('')
    v.set('')
b2=Button(w,text='Clear',font=('times new roman',15,'bold'),fg='white',bg='red',command=clear)
b2.place(x=270,y=300)

w.mainloop()
