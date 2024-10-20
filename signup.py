from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameentry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()==''or usernameentry.get()==''or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('error','All Fields are Required')
    elif passwordEntry.get()!=confirmEntry.get():
        messagebox.showerror('Error','Password Mismatched')

    elif check.get()==0:
        messagebox.showerror('error','Please accept Terms & conditions')   
    else:
        try:
             con=pymysql.connect(host='localhost',user='root',password='2003')   
             mycursor=con.cursor() 
        except:
            messagebox.showerror('error','Database Connectivity issue Please Try again')  
            return    
        try:
            query='create database userdata' 
            mycursor.execute(query)  
            query='use userdata' 
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(50),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')   

        query='select * from data where username =%s'
        mycursor.execute(query,(usernameentry.get())) 

        row=mycursor.fetchone()  
    
        if row !=None:
            messagebox.showerror('error','Username Already exixts')

        else:
             query='insert data(email,username,password) values(%s,%s,%s)'
             mycursor.execute(query,(emailEntry.get(),usernameentry.get(),passwordEntry.get()))
             con.commit()
             con.close()
             messagebox.showinfo('success','Registartion is Successful')  
             clear()
             signup_window.destroy()
             import  signin

def login_page():
    signup_window.destroy()
    import  signin

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='bg.jpg')

bglabel=Label(signup_window,image=background)
bglabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)
heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft yahei UI Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10 )
bgLabel=Label(signup_window)

emaillabel=Label(frame,text='Email',font=('Microsoft yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)



usernamelabel=Label(frame,text='Username',font=('Microsoft yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernamelabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameentry=Entry(frame,width=30,font=('Microsoft yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
usernameentry.grid(row=4,column=0,sticky='w',padx=25)



passwordlabel=Label(frame,text='password',font=('Microsoft yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordlabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)


confirmlabel=Label(frame,text='Confirm Password',font=('Microsoft yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmlabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=30,font=('Microsoft yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check =IntVar()

condition = Checkbutton(frame, text='I aggre to the Terms and Conditions', font=('Microsoft yahei ui light',9,'bold'), fg='firebrick1', bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
condition.grid(row=9,column=0,pady=10,padx=15)

#signup button
signup_button=Button(frame,text='Signup',font=('open sans',16,'bold'),fg='white',bg='firebrick1',width=17,activebackground='firebrick1',activeforeground='white',command=connect_database)
signup_button.grid(row=10,column=0,pady=10)

alreadyacc=Label(frame,text="Don't have an account",font=('open sans',9,'bold'),fg='firebrick1',bg='white')
alreadyacc.grid(row=11,column=0,sticky='w',padx=25,pady=10)

LoginButton=Button(frame,text='Log in',font=('open sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
LoginButton.place(x=170,y=408)


signup_window.mainloop()
