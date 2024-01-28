#This is our sign up page
from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

window.mainloop()

img = PhotoImage(file='Signup.jpg')
Label(window,image=img,border=0,bg='white').place(x=50,y=90)

frame=Frame(window,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)