#This is our sign up page

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk


window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)


bgOriginal = Image.open('Signup.jpg').resize((925,500))
# bgImage = ImageTk.PhotoImage(bgOriginal)
# bgLabel=Label(window,image=bgImage)
# bgLabel.place(x=0,y=0)S
img =ImageTk.PhotoImage(bgOriginal)
Label(window,image=img,border=0,bg='white').place(x=0,y=0)

frame=Frame(window,width=350,height=350,bg='white')
frame.place(x=500,y=50)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI',23,'bold'))
heading.grid(row=0,column=0)

user = Entry(frame,width=35,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',11))



window.mainloop()
#Jai Shree Ram   Datta Guru

