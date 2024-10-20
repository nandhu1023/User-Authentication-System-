from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#functional part

def forget_pass():
    def change_password():
        if userEntry.get()=='' or passwordEntry.get()==''or confirmpassEntry.get()=='':
           messagebox.showerror('Error','All Fields are Required',parent=window)
        elif passwordEntry.get()!=confirmpassEntry.get():
           messagebox.showerror('Error','Password and Confirm Password not matching',parent=window) 
        else:
            con=pymysql.connect(host='localhost',user='root',password='2003',database='userdata')
            mycursor=con.cursor()
            query='select * from data where username = %s'
            mycursor.execute(query,(userEntry.get()))
            row = mycursor.fetchone()

            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query= 'update data set password=%s where username=%s' 
                mycursor.execute(query,(passwordEntry.get(),userEntry.get()))   
                con.commit()
                con.close()
                messagebox.showinfo('success','Password is reset, Please Login with new password',parent=window) 
                window.destroy() 
      
    window = Toplevel()
    window.title('change password')

    bgPic= ImageTk.PhotoImage(file='background.jpg')
    bgLabel= Label(window, image=bgPic)
    bgLabel.grid()

    headingLabel=Label(window,text='RESET PASSWORD',font=('arial',18,'bold'),bg='white',fg='magenta2')
    headingLabel.place(x=480, y=60)

    userLabel= Label(window, text='username',font=('arial',12,'bold'),bg='white',fg='orchid1')
    userLabel.place(x=470 ,y=130)
    userEntry=Entry(window,width=25,font=('arial',11,'bold'),fg='magenta2',bd=0)
    userEntry.place(x=470,y=160)

    frame1=Frame(window,width=250,height=2,bg='orchid1')
    frame1.place(x=470,y=180)

    passwordLabel=Label(window,text='New Password',font=('arial',12,'bold'),bg='white',fg='orchid1')
    passwordLabel.place(x=470 ,y=210 )

    passwordEntry=Entry(window,width=25,font=('arial',11,'bold'),fg='magenta2',bd=0)
    passwordEntry.place(x=470 ,y=240)

    frame2=Frame(window,width=250,height=2,bg='orchid1')
    frame2.place(x=470, y=260)


    confirmpassLabel=Label(window,text='confirm Password',font=('arial',12,'bold'),bg='white',fg='orchid1')
    confirmpassLabel.place(x=470 ,y=290 )

    confirmpassEntry=Entry(window,width=25,font=('arial',11,'bold'),fg='magenta2',bd=0)
    confirmpassEntry.place(x=470 ,y=320)

    frame3=Frame(window,width=250,height=2,bg='orchid1')
    frame3.place(x=470, y=340)

    submitButton= Button(window, text='submit',bd=0,bg='magenta2',fg='white',font=('open sans',16,'bold'),width=19,cursor='hand2',activebackground='magenta1',activeforeground='white',command=change_password)
    submitButton.place(x=470,y=390)

    window.mainloop() 

def login_user():
    if usernameEntry.get()==''or password_enter=='':
            messagebox.showerror('Error','All Fields are Required')    
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='2003')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is Not Established Please Try Again')
            return
        
        query='use userdata'  
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))

        row=mycursor.fetchone()

        if row==None:
            messagebox.showerror('error','Invalid Username or Password')

        else:
            messagebox.showinfo('welcome','Login sucessfull')    

def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')  
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='password':
        passwordEntry.delete(0,END)        


#gui part
login_window = Tk()
login_window .geometry('900x600+50+50')
login_window .resizable(0,0)
login_window .title('Login Page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel =Label(login_window ,image=bgImage)

bgLabel.place(x=0,y=0)

heading= Label(login_window ,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window ,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry=Entry(login_window ,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window,text='Forgot Password',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1',command= forget_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='Login',font=('open sans',16,'bold'),bd=0,fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',cursor='hand2',width=19,command=login_user)
loginButton.place(x=578,y=350)

#or--
orLabel=Label(login_window,text='-------------- OR --------------',font=('open sans',16),bg='white',fg='firebrick1')
orLabel.place(x=583,y=400)

#logo---
facebook_logo=PhotoImage(file='facebook.png')
fblabel=Label(login_window,image=facebook_logo)
fblabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googlelabel=Label(login_window,image=google_logo)
googlelabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterlabel=Label(login_window,image=twitter_logo)
twitterlabel.place(x=740,y=440)

signupLabel=Label(login_window,text="Don't have an account?",font=('open sans', 9,'bold'),fg='firebrick1',bg='white' )
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('open sans',9,'bold'),bd=0,fg='blue',bg='white',activebackground='white',activeforeground='blue',cursor='hand2',command=signup_page)
newaccountButton.place(x=727,y=500)


login_window .mainloop()

