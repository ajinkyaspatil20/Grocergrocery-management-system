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


frame=Frame(window,width=500,height=500,bg='white')
frame.place(x=20,y=20)
heading=Label(frame,text='Profile',fg='black',font=('Microsoft Yahei UI',23,'bold'))
heading.place(x=140,y=20)

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

Button(window,width=20,pady=7,text='Back',bg='#006666',fg='white',border=0,).place(x=700,y=400)   

#image_path = 'profile.png'
#image = Image.open(image_path)
#photo = ImageTk.PhotoImage(image)
    
    # Create a label and add the image to it
#label = Label(frame, image=photo)
#label.pack()
    
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=100)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=200)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=300)
#frame=Frame(window,width=200,height=50,bg='black')
#frame.place(x=250,y=400)

window.mainloop()




