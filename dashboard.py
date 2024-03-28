from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
from PIL import Image

window=Tk()
window.title("Dashboard")
window.geometry('925x500+185+85')
window.configure(bg='#fff')
window.resizable(False,False)

def add_open():
    window.destroy()
    import add
def outofstock_open():
    window.destroy()
    import outofstock
def sellbackend_open():
    window.destroy()
    import sellbackend
def expirydate_open():
    window.destroy()
    import expirydate

def pro_open():
    window.destroy()
    import profileofuser

bgOriginal = Image.open('newbg.png').resize((925,500))
        # bgImage = ImageTk.PhotoImage(bgOriginal)
        # bgLabel=Label(fwindow,image=bgImage)
        # bgLabel.place(x=0,y=0)S
img =ImageTk.PhotoImage(bgOriginal)
Label(window,image=img,border=0,bg='white').place(x=0,y=0)

bgOriginal1 = Image.open('profile.png').resize((275,155))
img1 =ImageTk.PhotoImage(bgOriginal1)
profile=Button(window,image=img1,border=10,bg='teal',activebackground='#356466',command=pro_open).place(x=15,y=55) 


bgOriginal2 = Image.open('add1.png').resize((275,155))
img2 =ImageTk.PhotoImage(bgOriginal2)
add=Button(window,image=img2,border=10,bg='teal',activebackground='#356466',command=add_open).place(x=320,y=55)





bgOriginal3 = Image.open('stocks.png').resize((275,155))
img3 =ImageTk.PhotoImage(bgOriginal3)
Button(window,image=img3,border=10,bg='teal',activebackground='#356466',command=outofstock_open).place(x=625,y=55)

bgOriginal4 = Image.open('stats.png').resize((275,155))
img4 =ImageTk.PhotoImage(bgOriginal4)
Button(window,image=img4,border=10,bg='teal',activebackground='#356466').place(x=15,y=265)

bgOriginal5 = Image.open('bill.png').resize((275,155))
img5 =ImageTk.PhotoImage(bgOriginal5)
Button(window,image=img5,border=10,bg='teal',activebackground='#356466',command=sellbackend_open).place(x=320,y=265)

bgOriginal6 = Image.open('exp.png').resize((275,155))
img6 =ImageTk.PhotoImage(bgOriginal6)
Button(window,image=img6,border=10,bg='teal',activebackground='#356466',command=expirydate_open).place(x=625,y=265)

# Button(window,width=50,pady=7,image='user.png',bg='#006666',fg='white',border=0).place(x=35,y=204)
# Button(window,width=50,pady=7,image='add.png',bg='#006666',fg='white',border=0).place(x=95,y=204)
# Button(window,width=50,pady=7,image='stat.png',bg='#006666',fg='white',border=0).place(x=155,y=204)
# Button(window,width=50,pady=7,image='expiry.png',bg='#006666',fg='white',border=0).place(x=35,y=404)
# Button(window,width=50,pady=7,image='sell.png',bg='#006666',fg='white',border=0).place(x=95,y=404)
# Button(window,width=50,pady=7,image='stock.png',bg='#006666',fg='white',border=0).place(x=155,y=404)


window.mainloop()