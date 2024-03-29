from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

#baba honaaaaaaaaaaaaaaaaaaaaaaaaaaaaaanamoooooooooooooooooooooooooooooo

def toggle_password_visibilityp():
    if code.get():
        code.config(show="")
        # conf.config(show="")
    else:
        code.config(show="*")
        # conf.config(show="*")


window = Tk()
window.title("LogIn")
window.geometry('925x500+185+85')
window.configure(bg='#fff')
window.resizable(False, False)

def toggle_password_visibilityb():
    if show_password_var.get():
         code.config(show="")
       
    else:
         code.config(show="*")
       
        
        
show_password_var = BooleanVar()
show_password_var.set(False)

def login_user():
    if user.get() == '' or user.get() == 'Username' or code.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", 'Connection Failed With Database')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from dataofuser where name=%s and password=%s'
        mycursor.execute(query, (user.get(), code.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error", 'Invalid username or password')
        else:
            messagebox.showinfo("Welcome", "Login Successful")
            window.destroy()
            import dashboard


def forgot_password():
    def change_pass():
        if user.get() == '' or code.get() == '' or conf.get() == '':
            messagebox.showerror("Error", 'All Fields Are Required')
        elif code.get() != conf.get():
            messagebox.showerror("Error", 'New password and Confirm password MISMATCH!')
        else:
            con = pymysql.connect(host='localhost', user='root', password='root', database='userdata')
            mycursor = con.cursor()
            query = 'select * from dataofuser where name=%s'

            mycursor.execute(query, (user.get(),))

            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'User Does not Exist')
            else:
                query = 'update dataofuser set password =%s where name=%s'
                mycursor.execute(query, (code.get(), user.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is Reset')
                fwindow.destroy()

    fwindow = Toplevel()

    def user_enter(e):
        if user.get() == 'Username':
            user.delete(0, END)

    def code_enter(e):
        if code.get() == 'New Password':
            code.delete(0, END)

    def conf_enter(e):
        if conf.get() == 'Confirm Password':
            conf.delete(0, END)

    def user_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    def code_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'New Password')

    def conf_leave(e):
        name = conf.get()
        if name == '':
            conf.insert(0, 'Confirm Password')

    fwindow.title("LogIn")
    fwindow.geometry('925x500+300+150')
    fwindow.configure(bg='#fff')
    fwindow.resizable(False, False)

    bgOriginal = Image.open('new1.png').resize((925, 500))
    img = ImageTk.PhotoImage(bgOriginal)
    Label(fwindow, image=img, border=0, bg='white').place(x=0, y=0)

    frame = Frame(fwindow, width=300, height=300, bg='white')
    frame.place(x=550, y=65)

    heading = Label(frame, text='Reset Password', fg='#006666', bg='white', font=('Microsoft Yahei UI', 23, 'bold'))
    heading.place(x=27, y=20)

    user = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', user_enter)
    user.bind('<FocusOut>', user_leave)
    Frame(frame, width=246, height=2, bg='black').place(x=25, y=102)

    code = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
    code.place(x=30, y=130)
    code.insert(0, 'New Password')
    code.bind('<FocusIn>', code_enter)
    code.bind('<FocusOut>', code_leave)
    
    
    Frame(frame, width=246, height=2, bg='black').place(x=25, y=152)

    conf = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
    conf.place(x=30, y=180)
    conf.insert(0, 'Confirm Password')
    conf.bind('<FocusIn>', conf_enter)
    conf.bind('<FocusOut>', conf_leave)
    Frame(frame, width=246, height=2, bg='black').place(x=25, y=202)

    Button(frame, width=25, pady=7, text='RESET', bg='#006666', activebackground='#006666', activeforeground='white',
           fg='white', border=0, command=change_pass).place(x=60, y=250)
    
    # Checkbutton(frame, text='Show Password', command=toggle_password_visibilityp,bg='white',fg='#006666').place(x=175, y=215)
    
    fwindow.mainloop()


def sign_up_page():
    window.destroy()
    import signup


bgOriginal = Image.open('new1.png').resize((925, 500))
img = ImageTk.PhotoImage(bgOriginal)
Label(window, image=img, border=0, bg='white').place(x=0, y=0)

frame = Frame(window, width=350, height=350, bg='white')
frame.place(x=500, y=65)

heading = Label(frame, text='LogIn', fg='#006666', bg='white', font=('Microsoft Yahei UI', 23, 'bold'))
heading.place(x=120, y=20)



def user_enter(e):
    if user.get() == 'Username':
        user.delete(0, END)


def user_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
user.place(x=30, y=116)
user.insert(0, 'Username')
user.bind('<FocusIn>', user_enter)
user.bind('<FocusOut>', user_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=137)

def code_enter(e):
    if code.get() == 'Password':
        code.delete(0, END)
        toggle_password_visibilityp()


def code_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')
        if show_password_var.get():
         code.config(show="*")
        
        else:
         code.config(show="")


code = Entry(frame, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10), bd=0)
code.place(x=30, y=165)
code.insert(0, 'Password')
code.bind('<FocusIn>', code_enter)
code.bind('<FocusOut>', code_leave)


Button(frame, width=39, pady=7, text='Log In', bg='#006666', fg='white', border=0, command=login_user).place(x=35,
                                                                                                           y=250)

Button(frame, width=15, text='Forgot Password?', border=0, bg='white', cursor='hand2', fg='#006666',
       command=forgot_password).place(x=215, y=200)

# Checkbutton(frame, text='Show Password', command=toggle_password_visibilityp,bg='white',fg='#006666').place(x=215, y=225)
show_password_checkbox = Checkbutton(frame, text="Show Password", variable=show_password_var,
                                      command=toggle_password_visibilityb, bg='white', fg='#006666',
                                      activeforeground='#006666')
show_password_checkbox.place(x=215, y=225)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=187)

label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI', 10))
label.place(x=75, y=295)

Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='blue',
       activeforeground='#8c03fc', activebackground='white', command=sign_up_page).place(x=225, y=298)

window.mainloop()