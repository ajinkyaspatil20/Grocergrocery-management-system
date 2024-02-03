#This is our sign up page

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql


Vwindow=Tk()
Vwindow.title("SignUp")
Vwindow.geometry('925x500+300+150')
Vwindow.configure(bg='#fff')
Vwindow.resizable(False,False)


def direct_login():
    Vwindow.destroy()
    import login
    

def clear():
    user.delete(0,END)
    code.delete(0,END)
    conf.delete(0,END)
    check.set(0)



def login_page():

    if user.get() == "" or code.get() == "" or conf.get() == "" or user.get() == "Username" or code.get() == "Password" or conf.get() == "Confirm Password" :
        messagebox.showerror('Error','All Fields Are Required')
        
        
        
    
    elif conf.get() != code.get() :
        messagebox.showerror('Error','Password Mismatch')

    elif check.get() == 0 :
        messagebox.showerror('Error','Please Accept Terms and Conditions')
    
    else:
        try:
           con=pymysql.connect(host = 'localhost',user='root',password='travelmanagement')
           mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return
        try:
            query="create database userdata"
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table dataofuser(id int auto_increment primary key not null ,name varchar(50),password varchar(25))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
         #left1  
        query='select * from dataofuser where name=%s'

        mycursor.execute(query,(user.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','User Already Exist')
        else:



            query='insert into dataofuser(name ,password) values(%s,%s)'
            mycursor.execute(query,(user.get(),code.get() ))
            con.commit()
            con.close()
            messagebox.showinfo('Sucsess','Registration is Successful')
            clear()
            Vwindow.destroy()
            import login

    


bgOriginal = Image.open('new1.png').resize((925,500))
# bgImage = ImageTk.PhotoImage(bgOriginal)
# bgLabel=Label(Vwindow,image=bgImage)
# bgLabel.place(x=0,y=0)S
img =ImageTk.PhotoImage(bgOriginal)
Label(Vwindow,image=img,border=0,bg='white').place(x=0,y=0)

frame=Frame(Vwindow,width=350,height=350,bg='white')
frame.place(x=500,y=65)

heading=Label(frame,text='SignUp',fg='#006666',bg='white',font=('Microsoft Yahei UI',23,'bold'))
heading.place(x=120,y=20)

def user_enter(e):
   if user.get()=='Username':
    user.delete(0,END)

def code_enter(e):
   if code.get()=='Password':
    code.delete(0,END)

def conf_enter(e):
   if conf.get()=='Confirm Password':
    conf.delete(0,END)

def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user = Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10),bd=0)
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', user_enter)
user.bind('<FocusOut>', user_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)



def code_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10),bd=0)
code.place(x=30,y=120)
code.insert(0,'Password')
code.bind('<FocusIn>', code_enter)
code.bind('<FocusOut>', code_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=187)


Button(frame,width=39,pady=7,text='Sign Up',bg='#006666',fg='white',border=0,command=login_page).place(x=35,y=204)



Frame(frame,width=295,height=2,bg='black').place(x=25,y=147)


def conf_leave(e):
    name=conf.get()
    if name=='':
        conf.insert(0,'Confirm Password')
conf = Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10),bd=0)
conf.place(x=30,y=160)
conf.insert(0,'Confirm Password')
conf.bind('<FocusIn>', conf_enter)
conf.bind('<FocusOut>', conf_leave)
check=IntVar()
termsandcondtitions=Checkbutton(frame,bg='white',text='I Agree to the Terms and Conditions', font= ( 'Microsoft Yahei UI',9,'bold'), variable=check ,fg='#006666',activeforeground='#006666')
termsandcondtitions.place(x=50,y=240)

footer=Label(frame,text='Already have an Account?',fg='black',bg='white',font=('Microsoft Yahei UI',9,'italic'))
footer.place(x=50,y=270)

footer1=Button(frame,width=5,text='Log In',bg='white',fg='blue',activeforeground='#8c03fc',activebackground='white',border=0,command=direct_login).place(x=210,y=270)



Vwindow.mainloop()
#Jai Shree Ram   Datta Guru

# hello 123
#hello aj
#hello miniproject
#hello guys kam ho gya he!!!!
