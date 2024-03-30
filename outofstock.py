import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from tkcalendar import Calendar
import tkinter as tk
from docxtpl import DocxTemplate

mwindow=Tk()
mwindow.title=('Grocery Management System')
mwindow.geometry('1440x750+50+20')

bgOriginal = Image.open('newbg.png').resize((1500,800))
        # bgImage = ImageTk.PhotoImage(bgOriginal)
        # bgLabel=Label(fwindow,image=bgImage)
        # bgLabel.place(x=0,y=0)
img =ImageTk.PhotoImage(bgOriginal)
Label(mwindow,image=img,border=0,bg='white').place(x=0,y=0)
def backtodashboard():
    mwindow.destroy()
    import dashboard
    
    
def clear_entryfield():
    quan.delete(0,END)
    name.delete(0,END)
    exd.delete(0,END)
    
        
def add_details():
    try:
        con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
        mycursor= con.cursor()
    except:
        messagebox.showerror("Error",'Connection Failed With Database')
        return
    query='use crud'
    mycursor.execute(query)
    if quan.get()==''or exd.get()=='':
        messagebox.showerror("ERROR",'Please Enter Quantity AND Expiry date')
        return
    
   
    query="update finaldbt set quantity=%s,ex_date=%s where name =%s"
    mycursor.execute(query,(quan.get(),exd.get(),name.get()))
    
    con.commit()
    con.close()
    messagebox.showinfo("ADDED","PRODUCT ADDED SUCCESSFULLY")
    fetch_data()

    clear_entryfield()

def search():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    search_term = searche.get()
    if search_term:
        # Clear the current content of the treeview
        query="select w_name,w_contact,name,ex_date from finaldbt where quantity = 0"             #
        mycursor.execute(query)
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
        # for row in product_table.get_children():
        #     product_table.delete(row)
        # Execute SQL query to fetch names matching the search term
        mycursor.execute("SELECT w_name, w_contact, name, ex_date FROM finaldbt WHERE name LIKE %s AND (quantity = 0 OR quantity IS NULL)", (f'%{search_term}%',))

        row=mycursor.fetchall()
        
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
            for i in row:
                product_table.insert("",END,values=i)
            con.commit()
        else:
            messagebox.showerror("INVALID SEARCH","NO ITEM IN INVENTORY")
            searche.delete(0,END)
            query="select w_name,w_contact,name,ex_date from finaldbt where quantity = 0"
            mycursor.execute(query)
            row=mycursor.fetchall()
            if len(row)!=0:
                product_table.delete(*product_table.get_children())
                for i in row:
                    product_table.insert("",END,values=i)
                con.commit()
            con.close() 
        
    else:
        
        query="select w_name,w_contact,name,ex_date from finaldbt where quantity = 0"#
        mycursor.execute(query)
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
            for i in row:
                product_table.insert("",END,values=i)
            con.commit()
        con.close()  

def fetch_data():

    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    query="select w_name,w_contact,name,ex_date from finaldbt where quantity = 0 "
    mycursor.execute(query)
    row=mycursor.fetchall()
    if len(row)!=0:
        product_table.delete(*product_table.get_children())
        for i in row:
            product_table.insert("",END,values=i)
        con.commit()
    con.close() 
    
    
def get_cursor(event=''):

    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    cursor_row=product_table.focus()
    content=product_table.item(cursor_row)
    rowss=content["values"]
    name.delete(0,END)
    quan.delete(0,END)
    exd.delete(0,END)
    name.insert(0,rowss[2])



def open_cal():
    select.config(state=tk.DISABLED)
    def get_date():
        selected_date = cal.get_date()
        exd.delete(0,END)
        exd.insert(0,selected_date)
        root.destroy()
        select.config(state=tk.NORMAL)
    select.config(state=tk.NORMAL)    
        
    
    # You can do whatever you want with the selected date, such as updating a label or entry field

    root = tk.Tk()
    root.title("Date Picker")

    cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(padx=12, pady=12)

    btn=Button(root, text="Get Date", command=get_date)
    btn.pack(pady=5)
    

    root.mainloop()
      
head=Label(mwindow,text="OUTOF STOCK")
head.place(x=720,y=0)

"""head1=Label(mwindow,text="Search Product")
head1.place(x=100,y=30)"""
outputframe=Frame(mwindow,bd=10,relief=RIDGE)
outputframe.place(x=20,y=100,width=800,height=500)
head2=Label(mwindow,text="SEARCH : ")
head2.place(x=20,y=50)
searche = Entry(mwindow,width=48,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
searche.place(x=80,y=50)
searchb=Button(mwindow,width=10,text='SEARCH',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=search)
searchb.place(x=480,y=50)

#limith=Label(mwindow,text="SET LIMIT ACCORDINGLY")
#limith.place(x=690,y=30)
#limit=Label(mwindow,text="SET LIMIT : ")
#limit.place(x=620,y=50)
#limite = Entry(mwindow,width=48,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
#limite.place(x=690,y=50)
#limitb=Button(mwindow,width=10,text='APPLY',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=search)
#limitb.place(x=1090,y=50)

outputframe1=Frame(mwindow,bd=10,relief=GROOVE)
outputframe1.place(x=900,y=100,width=500,height=110)
#outputframe3=Frame(mwindow,bd=4,relief=RIDGE,pady=6)
#outputframe3.place(x=800,y=620,height=80,width=400)

#c_namel=Label(outputframe3,text='Name of customer:',bd=0)
#c_namel.grid(row=0,column=0,padx=20)
#c_namee = Entry(outputframe3,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
#c_namee.grid(row=0,column=1)

#c_contactl=Label(outputframe3,text='Customer contact:',bd=0)
#c_contactl.grid(row=1,column=0,padx=20)
#c_contacte = Entry(outputframe3,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
#c_contacte.grid(row=1,column=1)



product_table=ttk.Treeview(outputframe,columns=("whslname","contact","name_of_product","exdate"))

vsbp = ttk.Scrollbar(outputframe, orient="vertical", command=product_table.yview)
vsbp.pack(side="right", fill="y")
product_table.configure(yscrollcommand=vsbp.set)

hsbp = ttk.Scrollbar(outputframe, orient="horizontal", command=product_table.xview)
hsbp.pack(side="bottom", fill="x")
product_table.configure(xscrollcommand=hsbp.set)

product_table.heading("whslname",text="WHOLESALER")
product_table.heading("contact",text="CONTACT")
product_table.heading("name_of_product",text="PRODUCT") 
product_table.heading("exdate",text="EXPIRY DATE") 
#product_table.heading("discount",text="DISCOUNT") 
#product_table.heading("exdate",text="EXPIRY DATE") 

product_table["show"]="headings"
product_table.column("whslname",width=100)
product_table.column("contact",width=75)
product_table.column("name_of_product",width=50)
product_table.column("exdate",width=75)
#product_table.column("discount",width=50)
#product_table.column("exdate",width=75)
product_table.pack(fill=BOTH,expand=1)

product_table.bind("<ButtonRelease-1>",get_cursor)
fetch_data()

lb=Label(outputframe1,text='Name of product:',bd=0)
lb.grid(row=0,column=0,padx=20)
name = Entry(outputframe1,width=15,fg='black',border=2,bg="white",textvariable=1,font=('Microsoft Yahei UI',10))
name.grid(row=0,column=1)

lb1=Label(outputframe1,text='Quantity')
lb1.grid(row=1,column=0)
quan = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
quan.grid(row=1,column=1)

#lb4=Label(outputframe1,text="Total amount")
#lb4.grid(row=1,column=2,padx=20)
#stotal = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
#stotal.grid(row=1,column=3)

#lb5=Label(outputframe1,text="Selling price:")
#lb5.grid(row=1,column=0)
#sp = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
#sp.grid(row=1,column=1)

lb6=Label(outputframe1,text="Expiry date:")
lb6.grid(row=2,column=0)
exd = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
exd.grid(row=2,column=1)

add=Button(mwindow,width=20,padx=12,pady=0,text='ADD',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=add_details)
add.place(x=1070,y=230)

#update=Button(mwindow,width=15,pady=7,text='UPDATE',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=update_details)
#update.place(x=50,y=610)
#updatequantity=Entry(mwindow,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
#updatequantity.place(x=180,y=620)
#
#delete=Button(mwindow,width=15,pady=7,text='delete',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=delete_details)
#delete.place(x=325,y=610)

#print=Button(mwindow,width=15,pady=7,text='print',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=generate_invoice)
#print.place(x=1237,y=630)

#sell=Button(mwindow,width=15,pady=7,text='sell',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=sell_detail)
#sell.place(x=1237,y=670)
back=Button(mwindow,width=20,pady=7,text='DASHBOARD',bg='#013f45',activebackground='#006666',activeforeground='white',fg='white',border=1,command=backtodashboard).place(x=600,y=680)
select=Button(outputframe1,width=12,text='DATE',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=open_cal)
select.place(x=300,y=50)
mwindow.mainloop()