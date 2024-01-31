#This is our sign up page

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk


window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        print('ASYA')


bgOriginal = Image.open('Signup.jpg').resize((925,500))
# bgImage = ImageTk.PhotoImage(bgOriginal)
# bgLabel=Label(window,image=bgImage)
# bgLabel.place(x=0,y=0)S
img =ImageTk.PhotoImage(bgOriginal)
Label(window,image=img,border=0,bg='white').place(x=0,y=0)

frame=Frame(window,width=350,height=350,bg='white')
frame.place(x=500,y=65)

heading=Label(frame,text='Sign in',fg='#34e4e1',bg='white',font=('Microsoft Yahei UI',23,'bold'))
heading.place(x=120,y=30)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user = Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',11),bd=0)
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
   code.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',11),bd=0)
code.place(x=30,y=120)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=187)


Button(frame,width=39,pady=7,text='Sign in',bg='#34e4e1',fg='white',border=0).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft Yahei UI',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#34e4e1',command=signin)
sign_up.place(x=215,y=270)

def on_enter(e):
   conf.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        conf.insert(0,'Confirm Password')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=147)

conf = Entry(frame,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',11),bd=0)
conf.place(x=30,y=160)
conf.insert(0,'Confirm Password')
conf.bind('<FocusIn>', on_enter)
conf.bind('<FocusOut>', on_leave)




window.mainloop()
#Jai Shree Ram   Datta Guru

# hello 123
#hello aj
#hello miniproject
#hello guys kam ho gya he!!!!
