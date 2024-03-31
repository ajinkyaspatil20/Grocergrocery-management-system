from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from tkcalendar import Calendar
import tkinter as tk


window=Tk()
window.title("STATISTICS")
window.geometry('925x500+185+85')
window.configure(bg='#fff')
window.resizable(False,False)

def profits_open():
    window.destroy()
    import profits

def sales_open():
    window.destroy()
    import sales
def backtodashboard():
    window.destroy()
    import dashboard
bgOriginal = Image.open('newbg.png').resize((925,500))
        # bgImage = ImageTk.PhotoImage(bgOriginal)
        # bgLabel=Label(fwindow,image=bgImage)
        # bgLabel.place(x=0,y=0)
img =ImageTk.PhotoImage(bgOriginal)

Label(window,image=img,border=0,bg='white').place(x=0,y=0)

bgOriginal1 = Image.open('profits1.png').resize((325,200))
img5 =ImageTk.PhotoImage(bgOriginal1)
Button(window,image=img5,border=10,bg='teal',activebackground='#356466',command=profits_open).place(x=100,y=135)

bgOriginal2 = Image.open('sales1.png').resize((325,200))
img6 =ImageTk.PhotoImage(bgOriginal2)
Button(window,image=img6,border=10,bg='teal',activebackground='#356466',command=sales_open).place(x=500,y=135)

back=Button(window,width=20,pady=7,text='DASHBOARD',bg='#013f45',activebackground='#006666',activeforeground='white',fg='white',border=1,command=backtodashboard).place(x=600,y=460)


window.mainloop()