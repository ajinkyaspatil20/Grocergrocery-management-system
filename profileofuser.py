from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql


window = Tk()
window.title("PROFILE")
window.geometry("925x500+300+150")
window.configure(bg='#00FFFF')
window.resizable(False,False)

bgOriginal = Image.open('newbg.png').resize((925,500))
img =ImageTk.PhotoImage(bgOriginal)
Label(window,image=img,border=0,bg='white').place(x=0,y=0)

def backtodashboard():
    window.destroy()
    import dashboard
    
frame=Frame(window,width=500,height=460,bg='white')
frame.place(x=212,y=20)
heading=Label(frame,text='PROFILE',fg='black', bg="white" ,font=('Microsoft Yahei UI',23,'bold'))
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
def storedata():
    # i_storename=shop.get()
    # i_address=add.get()       make a new database
    

    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    query='select * from shopdetails where shopname=%s'

    mycursor.execute(query,(shop.get()))

    row=mycursor.fetchone()
    if row != None:
        messagebox.showerror('Error','SHOP Already Exist')
    else:
    
        query = 'INSERT INTO shopdetails (o_name, shopname, address, o_contact, email) VALUES (%s, %s, %s, %s, %s)'
        data = (user.get(), shop.get(), add.get(), cont.get(), email.get())
        mycursor.execute(query, data)
        con.commit()
        messagebox.showinfo("UPDATED","Profile Updated Successfully")
        
        user.delete(0,END)
        shop.delete(0,END)
        add.delete(0,END)
        cont.delete(0,END)
        email.delete(0,END)
        
        query='select o_name from shopdetails'
        mycursor.execute(query)
        nameofowner=mycursor.fetchone()
        nameofowner0=nameofowner[0]
        user.insert(0,nameofowner0)
        query='select shopname from shopdetails'
        mycursor.execute(query)
        nameofshop=mycursor.fetchone()
        nameofshop0=nameofshop[0]
        shop.insert(0,nameofshop0)
        query='select address from shopdetails'
        mycursor.execute(query)
        nameofadd=mycursor.fetchone()
        nameofadd0=nameofadd[0]
        add.insert(0,nameofadd0)
        query='select o_contact from shopdetails'
        mycursor.execute(query)
        nameofcon=mycursor.fetchone()
        nameofcon0=nameofcon[0]
        cont.insert(0,nameofcon0)
        query='select email from shopdetails'
        mycursor.execute(query)
        nameofem=mycursor.fetchone()
        nameofem0=nameofem[0]
        email.insert(0,nameofem0)
        con.close()
                
        
    
def user_enter(e):
    if user.get()=='Name':
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
    if shop.get()=='ShopName':
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
    if add.get()=='Address':
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
    if cont.get()=='Contact':
        cont.delete(0, END)


def con_leave(e):
    name = cont.get()
    if name == '':
        cont.insert(0, 'Contact')


cont = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
cont.place(x=200, y=300)
cont.insert(0, 'Contact')
cont.bind('<FocusIn>', con_enter)
cont.bind('<FocusOut>', con_leave)
Frame(frame, width=245, height=2, bg='black').place(x=200, y=325)

#Email
def email_enter(e):
    if email.get()=='Email':
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

Button(frame, width=39, pady=7, text='Update Profile', bg='#006666', fg='white', border=0,command=storedata).place(x=115,y=400)
back=Button(window,width=20,pady=7,text='DASHBOARD',bg='#013f45',activebackground='#006666',activeforeground='white',fg='white',border=1,command=backtodashboard).place(x=750,y=450)








#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=100)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=200)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=300)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=400)

window.mainloop()