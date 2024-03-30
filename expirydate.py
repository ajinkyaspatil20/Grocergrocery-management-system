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


def applylimit():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    limitno=int(limite.get())
    query = "SELECT name, s_price, quantity, s_total, discount, ex_date FROM finaldbt WHERE ex_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL %s DAY) ORDER BY ex_date"
    mycursor.execute(query,limitno)
    row=mycursor.fetchall()
    if len(row)!=0:
        product_table.delete(*product_table.get_children())
        for i in row:
            product_table.insert("",END,values=i)
        con.commit()
    con.close() 
def applylimit1():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    enddate=limite1.get()
    query ="SELECT name, s_price, quantity, s_total, discount, ex_date FROM finaldbt WHERE ex_date BETWEEN CURDATE() AND %s ORDER BY ex_date"

    mycursor.execute(query,(enddate))
    row=mycursor.fetchall()
    if len(row)!=0:
        product_table.delete(*product_table.get_children())
        for i in row:
            product_table.insert("",END,values=i)
        con.commit()
    con.close() 
    

def on_vertical_scroll(*args):
    outputframe.yview(*args)
def on_horizontal_scroll(*args):
    outputframe.xview(*args)
def backtodashboard():
    mwindow.destroy()
    import dashboard
    

    

        
def clear_entryfield():
    quan.delete(0,END)
    name.delete(0,END)
    stotal.delete(0,END)
    sp.delete(0,END)
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
    
    if quan.get()=='':
        messagebox.showerror("Error",'Please Enter The DISCOUNT IN % ')
        return

    discount = float (quan.get())
    #can be takend by database also in add
    sp_value = float(sp.get())  
    new_sp_value = sp_value-((discount / 100) * sp_value)
    
    query="select quantity from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    
    quantity = mycursor.fetchone()
    quanttity=float(quantity[0])
    stotal = new_sp_value * quanttity
    
    query="update finaldbt set s_price=%s ,s_total=%s,discount=%s where name =%s"
    mycursor.execute(query,(new_sp_value,stotal,discount,name.get()))
    con.commit()
    fetch_data()
    con.close()
    messagebox.showinfo('Sucsess',' Item UPDATED Successfully')
    clear_entryfield()

def clear_entryfield():
    quan.delete(0,END)
    name.delete(0,END)
    stotal.delete(0,END)
    sp.delete(0,END)
    exd.delete(0,END)

  
def search():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    search_term = searche.get()
    if search_term:
        # Clear the current content of the treeview
        query="SELECT name, s_price, quantity, s_total, discount, ex_date FROM finaldbt ORDER BY ex_date"             #
        mycursor.execute(query)
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
        # for row in product_table.get_children():
        #     product_table.delete(row)
        # Execute SQL query to fetch names matching the search term
        mycursor.execute("SELECT name,s_price,quantity,s_total,discount,ex_date FROM finaldbt WHERE name LIKE %s ORDER BY ex_date", (f'%{search_term}%',))
        row = mycursor.fetchall()

        
        if len(row) != 0:
            product_table.delete(*product_table.get_children())
            for row in row:
                # Compare the date directly with today's date
                ex_date = row[5]
                if ex_date < datetime.date.today():
                    product_table.insert("", END, values=row, tags=("red_row",))
                else:
                    product_table.insert("", END, values=row)
                con.commit()
        else:
            messagebox.showerror("INVALID SEARCH","NO ITEM IN INVENTORY")
            searche.delete(0,END)
            fetch_data()
            
        
    else:
        fetch_data()
        
    

def fetch_data():

    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    # query = "SELECT name, s_price, quantity, s_total, discount, ex_date FROM finaldbt ORDER BY TIMESTAMPDIFF(DAY, CURDATE(), ex_date)"
    # mycursor.execute(query)
    # row=mycursor.fetchall()
    # if len(row)!=0:
    #     product_table.delete(*product_table.get_children())
    #     for i in row:
    #         product_table.insert("",END,values=i)
    #     con.commit()
    # con.close()
    query = "SELECT name, s_price, quantity, s_total, discount, ex_date FROM finaldbt ORDER BY ex_date"
    mycursor.execute(query)

    rows = mycursor.fetchall()

    if len(rows) != 0:
        product_table.delete(*product_table.get_children())
        for row in rows:
            # Compare the date directly with today's date
            ex_date = row[5]
            if row[4] is not None and row[4] != 0:
                product_table.insert("", END, values=row, tags=("yellow_row",))
            elif ex_date < datetime.date.today():
                product_table.insert("", END, values=row, tags=("red_row",))
            else:
                product_table.insert("", END, values=row)
        con.commit()

    con.close()


    
    
    
    
def get_cursor(event=''):
    name.config(state='normal')
    sp.config(state='normal')
    exd.config(state='normal')
    stotal.config(state='normal')
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    cursor_row=product_table.focus()
    content=product_table.item(cursor_row)
    rowss=content["values"]
    name.delete(0,END)
    sp.delete(0,END)
    quan.delete(0,END)
    stotal.delete(0,END)
    exd.delete(0,END)
    name.insert(0,rowss[0])
    sp.insert(0,rowss[1])
    quan.insert(0,rowss[2])
    quan.delete(0,END)
    stotal.insert(0,rowss[3])
    exd.insert(0,rowss[5])
    name.config(state='disabled')
    sp.config(state='disabled')
    exd.config(state='disabled')
    stotal.config(state='disabled')


 


def open_cal():
    select.config(state=tk.DISABLED)
    def get_date():
        selected_date = cal.get_date()
        limite1.delete(0,END)
        limite1.insert(0,selected_date)
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

head=Label(mwindow,text="EXPIRY SECTION")
head.place(x=600,y=0)
head1=Label(mwindow,text="SELECT PRODUCTS TO BE SOLD")
head1.place(x=100,y=30)
outputframe=Frame(mwindow,bd=10,relief=RIDGE)
outputframe.place(x=20,y=250,width=1400,height=400)
head2=Label(mwindow,text="SEARCH : ")
head2.place(x=20,y=50)
searche = Entry(mwindow,width=48,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
searche.place(x=80,y=50)
searchb=Button(mwindow,width=10,text='SEARCH',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=search)
searchb.place(x=480,y=50)

limith=Label(mwindow,text="SET LIMIT ACCORDINGLY")
limith.place(x=690,y=30)
limit=Label(mwindow,text="SET LIMIT : ")
limit.place(x=620,y=50)
limite = Entry(mwindow,width=48,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
limite.place(x=690,y=50)
limitb=Button(mwindow,width=10,text='APPLY',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=applylimit)
limitb.place(x=1090,y=50)

limith1=Label(mwindow,text="SET LIMIT ACCORDINg TO DATE")
limith1.place(x=690,y=80)
limit1=Label(mwindow,text="SET LIMIT : ")
limit1.place(x=620,y=100)
limite1 = Entry(mwindow,width=48,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
limite1.place(x=690,y=100)
limitb1=Button(mwindow,width=10,text='APPLY',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=applylimit1)
limitb1.place(x=1090,y=100)
select=Button(mwindow,width=12,text='DATE',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=open_cal)
select.place(x=1200,y=100)

outputframe1=Frame(mwindow,bd=10,relief=GROOVE)
outputframe1.place(x=300,y=150,width=600,height=100)
#outputframe3=Frame(mwindow,bd=4,relief=RIDGE,pady=6)
#outputframe3.place(x=800,y=620,height=80,width=400)

#c_namel=Label(outputframe3,text='Name of customer:',bd=0)
#_namel.grid(row=0,column=0,padx=20)
#c_namee = Entry(outputframe3,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
#c_namee.grid(row=0,column=1)

#c_contactl=Label(outputframe3,text='Customer contact:',bd=0)
#c_contactl.grid(row=1,column=0,padx=20)
#c_contacte = Entry(outputframe3,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
#c_contacte.grid(row=1,column=1)

scroll_x=ttk.Scrollbar(outputframe,orient=HORIZONTAL, command=on_vertical_scroll)
scroll_y=ttk.Scrollbar(outputframe,orient=VERTICAL ,command=on_horizontal_scroll)


product_table=ttk.Treeview(outputframe,columns=("name_of_product","sellingprice","quantity","sellingpricetotal","discount","exdate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x=ttk.Scrollbar(command=product_table.xview)
scroll_y=ttk.Scrollbar(command=product_table.yview)

product_table.heading("name_of_product",text="PRODUCT")
product_table.heading("sellingprice",text="SELLING PRICE")
product_table.heading("quantity",text="QUANTITY") 
product_table.heading("sellingpricetotal",text="SELLING PRICE TOTAL") 
product_table.heading("discount",text="DISCOUNT") 
product_table.heading("exdate",text="EXPIRY DATE") 

product_table["show"]="headings"
product_table.column("name_of_product",width=100)
product_table.column("sellingprice",width=75)
product_table.column("quantity",width=50)
product_table.column("sellingpricetotal",width=75)
product_table.column("discount",width=50)
product_table.column("exdate",width=75)
product_table.pack(fill=BOTH,expand=1)

product_table.bind("<ButtonRelease-1>",get_cursor)
fetch_data()
product_table.tag_configure("red_row", background="red")  
product_table.tag_configure("yellow_row", background="yellow")

lb=Label(outputframe1,text='Name of product:',bd=0)
lb.grid(row=0,column=0,padx=20)
name = Entry(outputframe1,width=15,fg='black',border=2,bg="white",textvariable=1,font=('Microsoft Yahei UI',10))
name.grid(row=0,column=1)

lb1=Label(outputframe1,text='Discount:')
lb1.grid(row=0,column=2)
quan = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
quan.grid(row=0,column=3)

lb4=Label(outputframe1,text="Total amount")
lb4.grid(row=1,column=2,padx=20)
stotal = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
stotal.grid(row=1,column=3)

lb5=Label(outputframe1,text="Selling price:")
lb5.grid(row=1,column=0)
sp = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
sp.grid(row=1,column=1)

lb6=Label(outputframe1,text="Expiry date:")
lb6.grid(row=2,column=0)
exd = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
exd.grid(row=2,column=1)

add=Button(outputframe1,width=20,padx=12,pady=0,text='ADD',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=add_details)
add.place(x=300,y=52)

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

mwindow.mainloop()