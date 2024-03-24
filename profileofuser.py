from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql


window = Tk()
window.title("Profile")
window.geometry("925x500+300+150")
window.configure(bg='#00FFFF')
window.resizable(False,False)

bgOriginal = Image.open('newbg.png').resize((925,500))
img =ImageTk.PhotoImage(bgOriginal)
Label(window,image=img,border=0,bg='white').place(x=0,y=0)


frame=Frame(window,width=500,height=460,bg='white')
frame.place(x=212,y=20)
heading=Label(frame,text='Profile',fg='black', bg="white" ,font=('Microsoft Yahei UI',23,'bold'))
heading.place(x=200,y=20)

label=Label(frame,text="Name",fg='#006666',bg='white',font=('Microsoft Yahei UI',15))
label.place(x=50,y=150)

label=Label(frame,text="Shop Name",fg='#006666',bg='white',font=('Microsoft Yahei UI',15))
label.place(x=50,y=200)

label=Label(frame,text="Address",fg='#006666',bg='white',font=('Microsoft Yahei UI',15))
label.place(x=50,y=250)

label=Label(frame,text="Contact",fg='#006666',bg='white',font=('Microsoft Yahei UI',15))
label.place(x=50,y=300)

label=Label(frame,text="Email",fg='#006666',bg='white',font=('Microsoft Yahei UI',15))
label.place(x=50,y=350)

#bgOriginal = Image.open('sell.png').resize((100,100))
#img =ImageTk.PhotoImage(bgOriginal)
#Label(label,image=img,border=0,bg='white').place(x=30,y=30)



#image_path = 'profile.png'
#image = Image.open(image_path)
#photo = ImageTk.PhotoImage(image)
    
    # Create a label and add the image to it
#label = Label(frame, image=photo)def user_enter(e):


#name
def user_enter(e):
    user.delete(0, END)


def user_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Name')


user = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
user.place(x=200, y=150)
user.insert(0, 'Name')
user.bind('<FocusIn>', user_enter)
user.bind('<FocusOut>', user_leave)
Frame(frame, width=245, height=2, bg='black').place(x=200, y=175)

#shopname
def shop_enter(e):
    shop.delete(0, END)


def shop_leave(e):
    name = shop.get()
    if name == '':
        shop.insert(0, 'ShopName')


shop = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
shop.place(x=200, y=200)
shop.insert(0, 'ShopName')
shop.bind('<FocusIn>', shop_enter)
shop.bind('<FocusOut>', shop_leave)
Frame(frame, width=245, height=2, bg='black').place(x=200, y=225)

#Address
def add_enter(e):
    add.delete(0, END)


def add_leave(e):
    name = add.get()
    if name == '':
        add.insert(0, 'Address')


add = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
add.place(x=200, y=250)
add.insert(0, 'Address')
add.bind('<FocusIn>', add_enter)
add.bind('<FocusOut>', add_leave)
Frame(frame, width=245, height=2, bg='black').place(x=200, y=275)

#Contact
def con_enter(e):
    con.delete(0, END)


def con_leave(e):
    name = con.get()
    if name == '':
        con.insert(0, 'Contact')


con = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
con.place(x=200, y=300)
con.insert(0, 'Contact')
con.bind('<FocusIn>', con_enter)
con.bind('<FocusOut>', con_leave)
Frame(frame, width=245, height=2, bg='black').place(x=200, y=325)

#Email
def email_enter(e):
    email.delete(0, END)


def email_leave(e):
    name = email.get()
    if name == '':
        email.insert(0, 'Email')


email = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
email.place(x=200, y=350)
email.insert(0, 'Email')
email.bind('<FocusIn>', email_enter)
email.bind('<FocusOut>', email_leave)
Frame(frame, width=245, height=2, bg='black').place(x=200, y=375)

Button(frame, width=39, pady=7, text='Update Profile', bg='#006666', fg='white', border=0,).place(x=115,y=400)







#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=100)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=200)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=300)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=400)

window.mainloop()