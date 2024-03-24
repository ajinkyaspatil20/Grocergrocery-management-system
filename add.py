from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from tkcalendar import Calendar
import tkinter as tk


window=Tk()
window.title("Add")
window.geometry('925x500+185+85')
window.configure(bg='#fff')
window.resizable(False,False)

bgOriginal = Image.open('fruits.png').resize((925,500))
        # bgImage = ImageTk.PhotoImage(bgOriginal)
        # bgLabel=Label(fwindow,image=bgImage)
        # bgLabel.place(x=0,y=0)
img =ImageTk.PhotoImage(bgOriginal)
Label(window,image=img,border=0,bg='white').place(x=0,y=0)


def set_transparent(widget):
    widget.attributes('-alpha',0.0)

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

frame=Frame(window,width=750,height=185,bg="white")
frame.place(x=100,y=270)

lb=Label(window,text='PRODUCT NAME',bg="white",font=('Microsoft Yahei UI',10),fg="#013f45")
lb.place(x=310,y=275)
name = Entry(window,width=20,fg='black',border=2,bg="white",textvariable=1,font=('Microsoft Yahei UI',12))
name.place(x=425,y=275)



lb1=Label(window,text='Quantity',bg="white",font=('Microsoft Yahei UI',10),fg="#013f45")
lb1.place(x=500,y=320)
quan = Entry(window,width=20,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',12))
quan.place(x=625,y=320)


lb2=Label(window,text='Cost price',bg="white",font=('Microsoft Yahei UI',10),fg="#013f45")
lb2.place(x=125,y=320)
cp = Entry(window,width=20,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',12))
cp.place(x=270,y=320)

lb3=Label(window,text="Wholeseller's name",bg="white",font=('Microsoft Yahei UI',10),fg="#013f45")
lb3.place(x=500,y=370)
w_name = Entry(window,width=20,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',12))
w_name.place(x=625,y=370)

lb4=Label(window,text="Wholeseller's contact",bg="white",font=('Microsoft Yahei UI',10),fg="#013f45")
lb4.place(x=125,y=370)
w_contact = Entry(window,width=20,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',12))
w_contact.place(x=270,y=370)

lb5=Label(window,text="Selling price",bg="white",font=('Microsoft Yahei UI',10),fg="#013f45")
lb5.place(x=500,y=420)
sp = Entry(window,width=20,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',11))
sp.place(x=625,y=420)

lb6=Label(window,text="Expiry date",bg="white",font=('Microsoft Yahei UI',10),fg="#013f45")
lb6.place(x=125,y=420)
exd = Entry(window,width=10,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',11))
exd.place(x=270,y=420)

select=Button(window,width=12,text='DATE',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=open_cal)
select.place(x=370,y=420)

frame=Frame(window,width=850,height=225,bg="white")
frame.place(x=50,y=30)

def update_details():
    con=pymysql.connect(host='localhost',user='root',password='root')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    cp_value = float(cp.get())  
    quan_value = int(quan.get())  
    ctotal = cp_value * quan_value
    sp_value = float(sp.get())  
    quan_value = int(quan.get())  
    stotal = sp_value * quan_value

        
    query='update finaldbt set w_name=%s,w_contact=%s,c_price=%s,s_price=%s,quantity=%s,ex_date=%s,c_total=%s,s_total=%s where name =%s'
    mycursor.execute(query,(w_name.get(),w_contact.get(),cp.get(),sp.get(),quan.get(),exd.get(),ctotal,stotal,name.get() ))
    con.commit()
    fetch_data()
    con.close()

def get_cursor(event=''):
    update=Button(window,width=20,pady=7,text='UPDATE',bg='#013f45',activebackground='#006666',activeforeground='white',fg='white',border=1,command=update_details).place(x=370,y=460)
   
    
    delete=Button(window,width=20,pady=7,text='DELETE',bg='#013f45',activebackground='#006666',activeforeground='white',fg='white',border=1,command=delete_details).place(x=550,y=460)
   
    con=pymysql.connect(host='localhost',user='root',password='root')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    cursor_row=product_table.focus()
    content=product_table.item(cursor_row)
    rowss=content["values"]
    name.delete(0,END)
    w_name.delete(0,END)
    w_contact.delete(0,END)
    cp.delete(0,END)
    sp.delete(0,END)
    quan.delete(0,END)
    exd.delete(0,END)
    
    
    
    name.insert(0,rowss[0])
    w_name.insert(0,rowss[1])
    w_contact.insert(0,rowss[2])
    cp.insert(0,rowss[3])
    sp.insert(0,rowss[4])
    quan.insert(0,rowss[5])
    exd.insert(0,rowss[9])

def add_details():
    try:
        con=pymysql.connect(host='localhost',user='root',password='root')
        mycursor= con.cursor()
    except:
        messagebox.showerror("Error",'Connection Failed With Database')
        return
    query='use crud'
    mycursor.execute(query)
    
    
    query='select * from finaldbt where name=%s'

    mycursor.execute(query,(name.get()))

    row=mycursor.fetchone()
    if row != None:
        messagebox.showerror('Error','Product Already Exist')
    else:
        cp_value = float(cp.get())  
        quan_value = int(quan.get())  
        ctotal = cp_value * quan_value
        sp_value = float(sp.get())  
        quan_value = int(quan.get())  
        stotal = sp_value * quan_value

        
        query='insert into finaldbt(name ,w_name,w_contact,c_price,s_price,quantity,ex_date,c_total,s_total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query,(name.get(),w_name.get(),w_contact.get(),cp.get(),sp.get(),quan.get(),exd.get(),ctotal,stotal ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo('Sucsess',' Item Added Successfully')

def delete_details():
    con=pymysql.connect(host='localhost',user='root',password='root')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    query="delete from finaldbt where name =%s"
    mycursor.execute(query,name.get())
    con.commit()
    name.delete(0,END)
    w_name.delete(0,END)
    w_contact.delete(0,END)
    cp.delete(0,END)
    sp.delete(0,END)
    quan.delete(0,END)
    exd.delete(0,END)
    fetch_data()
    
    con.close()

def on_vertical_scroll(*args):
    window.yview(*args)

def on_horizontal_scroll(*args):
    window.xview(*args)

scroll_x=ttk.Scrollbar(frame,orient=HORIZONTAL, command=on_vertical_scroll)
scroll_y=ttk.Scrollbar(frame,orient=VERTICAL ,command=on_horizontal_scroll)

product_table=ttk.Treeview(frame,columns=("ProductName","wholesellername","wholesellercontact","costprice","sellingprice","quantity","costpricetotal","sellingpricetotal","discount","exdate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x=ttk.Scrollbar(command=product_table.xview)
scroll_y=ttk.Scrollbar(command=product_table.yview)
product_table.heading("ProductName",text="PRODUCT")
product_table.heading("wholesellername",text="WHOLESELLER NAME ")
product_table.heading("wholesellercontact",text="WHOLESELLER CONTACT")
product_table.heading("costprice",text="COST PRICE")
product_table.heading("sellingprice",text="SELLING PRICE")
product_table.heading("quantity",text="QUANTITY") 
product_table.heading("costpricetotal",text="COST PRICE TOTAL") 
product_table.heading("sellingpricetotal",text="SELLING PRICE TOTAL") 
product_table.heading("discount",text="DISCOUNT") 
product_table.heading("exdate",text="EXPIRY DATE") 

product_table["show"]="headings"
product_table.column("ProductName",width=100)
product_table.column("wholesellername",width=100)
product_table.column("wholesellercontact",width=100)
product_table.column("costprice",width=75)
product_table.column("sellingprice",width=75)
product_table.column("quantity",width=50)
product_table.column("costpricetotal",width=75)
product_table.column("sellingpricetotal",width=75)
product_table.column("discount",width=50)
product_table.column("exdate",width=75)
product_table.pack(fill=BOTH,expand=1)

product_table.bind("<ButtonRelease-1>",get_cursor)

def fetch_data():
    con=pymysql.connect(host='localhost',user='root',password='root')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    query="select * from finaldbt"
    mycursor.execute(query)
    row=mycursor.fetchall()
    if len(row)!=0:
        product_table.delete(*product_table.get_children())
        for i in row:
            product_table.insert("",END,values=i)
        con.commit()
    con.close()

fetch_data()

add=Button(window,width=20,pady=7,text='ADD',bg='#013f45',activebackground='#006666',activeforeground='white',fg='white',border=1,command=add_details).place(x=200,y=460)


window.mainloop()