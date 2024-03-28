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
    window.destroy()
    import dashboard
    
def merge_billing_data():
    merged_data = {}
    for item in expiry.get_children():
        values = expiry.item(item, 'values')
        name_of_product = values[0]
        quantity = int(values[2])
        if name_of_product in merged_data:
            merged_data[name_of_product]['quantity'] += quantity
        else:
            merged_data[name_of_product] = {
                'name_of_product': name_of_product,
                'sellingprice': values[1],
                'quantity': quantity,
                'discount': values[3],
                'exdate': values[4],
                'total': values[5]
            }
     # Clear existing data in billing table
    for item in expiry.get_children():
        expiry.delete(item)
    # Insert merged data into billing table
    for data in merged_data.values():
        expiry.insert('', 'end', values=(
            data['name_of_product'],
            data['sellingprice'],
            data['quantity'],
            data['discount'],
            data['exdate'],
            data['total']
        ))

def on_vertical_scroll(*args):
    outputframe.yview(*args)
def on_horizontal_scroll(*args):
    outputframe.xview(*args)

def sell_detail():   
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    # query="DELETE FROM graph WHERE date = CURDATE() "
    if not expiry.get_children():
        messagebox.showerror("ERROR",'Billing Table Empty')
        return
    try:
        query="INSERT INTO graph (date,profit,loss,nos) VALUES (CURDATE(),0.0,0.0,0)"
        mycursor.execute(query)
    except:
        messagebox.showinfo("INFO",'HELLO THERE')
    for row in expiry.get_children():
        # Extract data from the treeview
        name_of_product = expiry.item(row)['values'][0]
        
        query="select c_price from finaldbt where name=%s"
        mycursor.execute(query,name_of_product)
        cp=mycursor.fetchone()
        cp_f=float(cp[0])
        
        query="select s_price from finaldbt where name=%s"
        mycursor.execute(query,name_of_product)
        sp=mycursor.fetchone()
        sp_f=float(sp[0])
        
        
        query="select quantity from finaldbt where name=%s"
        mycursor.execute(query,name_of_product)
        pquantity=mycursor.fetchone()
        quantint1=int(pquantity[0])
        
        quantity = expiry.item(row)['values'][2]
        quantint2=int(quantity)
        finalquantity=quantint1-quantint2
        profit_f=(sp_f-cp_f)*quantint2
        # Execute SQL update statement
        sql = "UPDATE finaldbt SET quantity = %s WHERE name = %s"
        val = (finalquantity, name_of_product)
        mycursor.execute(sql, val)
        query="select profit from graph where date = CURDATE() "
        mycursor.execute(query)
        profit_t=mycursor.fetchone()
        profit_tf=float(profit_t[0])
        query="select nos from graph where date = CURDATE() "
        mycursor.execute(query)
        nos_t=mycursor.fetchone()
        nos_tf=int(nos_t[0])
        final_nos = nos_tf + 1
        final_nos_f = final_nos
        final_profit= profit_f + profit_tf
        final_profit_f=float(final_profit)
        sql = "UPDATE graph SET profit = %s WHERE date = CURDATE() "
        val = (final_profit_f)
        mycursor.execute(sql, val)
        sql = "UPDATE graph SET nos = %s WHERE date = CURDATE() "
        val = (final_nos_f)
        mycursor.execute(sql, val)
    con.commit()    
    fetch_data()    
    con.close()
    messagebox.showinfo('Sucsess',' Product SOLD')
    clear_entryfield
    for item in expiry.get_children():
        expiry.delete(item)
    
def delete_details():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    # Get the currently selected item
    selected_item = expiry.focus()
    # Delete the selected item
    if selected_item:
        expiry.delete(selected_item)
    
def generate_invoice():
    if c_contacte.get()=='' or c_namee.get()=="":
        messagebox.showerror("Error",'Please Enter The Name and Contact of the Customer')
        return
    doc = DocxTemplate("miniproject.docx")
    i_name= c_namee.get()
    i_contact= c_contacte.get()
    data = []
    for item in expiry.get_children():
        values = expiry.item(item, 'values')
        data.append(list(values))
    # Assuming item[5] contains string representations of numbers
    subtotal = sum(float(item[5]) for item in data)
    salestax = 0.18   #18%
    subttotal = subtotal * (1 + salestax)
    doc.render({"name":i_name,
                "phone":i_contact,
                "invoice_list":data,
                "subtotal":subtotal,
                "salestax":"18%",
                "total":subttotal})
    doc_name = "new_invoice" + str(i_name) + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    data.clear
        
def clear_entryfield():
    quan.delete(0,END)
    name.delete(0,END)
    stotal.delete(0,END)
    sp.delete(0,END)
    exd.delete(0,END)
    updatequantity.delete(0,END)
        
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
        messagebox.showerror("Error",'Please Enter The Quantity')
        return
    namev=name.get()
    quantityv=quan.get()
    query="select quantity from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    quantityq=mycursor.fetchone()
    quantint=int(quantityq[0])
    quantinte=int(quantityv)
    if quantint < quantinte :
        messagebox.showerror('Error','NOT ENOUGH STOCK(REENTER QUANTITY)')
        return
    query="select discount from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    discountv=mycursor.fetchone()
    sellingp=sp.get()
    query="select ex_date from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    date=mycursor.fetchone()
    total=float(quantityv) * float(sellingp)
    con.commit()
    for item in expiry.get_children():
        values = expiry.item(item, 'values')
        if values[0] == namev:
            # Update quantity and total
            new_quantity = int(values[2]) + int(quantinte)
            if quantint < new_quantity :
                messagebox.showerror('Error','NOT ENOUGH STOCK(REENTER QUANTITY)')
                return
            new_total = float(values[5]) + total
            expiry.item(item, values=(values[0], values[1], new_quantity, values[3], values[4], new_total))
            break
    else:
        # Insert new row
        expiry.insert('', 'end', values=(namev, sellingp, quantityv, discountv, date, total))
    # Merge data to combine rows with the same product name
    merge_billing_data()
    # Clear entry fields
    clear_entryfield()
   # expiry.insert("", "end", values=(namev,sellingp,quantityv,discountv,date,total))
    product_table.selection_remove(product_table.selection())
    clear_entryfield()

def search():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    search_term = searche.get()
    if search_term:
        # Clear the current content of the treeview
        query="select * from finaldbt"
        mycursor.execute(query)
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
        # for row in product_table.get_children():
        #     product_table.delete(row)
        # Execute SQL query to fetch names matching the search term
        mycursor.execute("SELECT * FROM finaldbt WHERE name LIKE %s", (f'%{search_term}%',))
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
            for i in row:
                product_table.insert("",END,values=i)
            con.commit()
        con.close() 
    else:
        
        query="select * from finaldbt"
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
    query="select name,s_price,quantity,s_total,discount,ex_date from finaldbt"
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

def get_cursor2(event=''):

    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    cursor_row=expiry.focus()
    content=expiry.item(cursor_row)
    rowss=content["values"]
    name.delete(0,END)
    sp.delete(0,END)
    quan.delete(0,END)
    stotal.delete(0,END)
    exd.delete(0,END)
    name.insert(0,rowss[0])
    sp.insert(0,rowss[1])
    quan.insert(0,rowss[2])
    stotal.insert(0,rowss[5])
    exd.insert(0,rowss[4])  
   
def update_details():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    # Get the currently selected item
    selected_item = expiry.focus()
    query="select discount from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    discountv=mycursor.fetchone()
    if updatequantity.get()=='':
        messagebox.showerror("Error",'Please Enter The Quantity')
        return
    namev=name.get()
    quantityv=updatequantity.get()
    query="select quantity from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    quantityq=mycursor.fetchone()
    quantint=int(quantityq[0])
    quantinte=int(quantityv)
    if quantint < quantinte :
        messagebox.showerror('Error','NOT ENOUGH STOCK(REENTER QUANTITY)')
        return
    query="select discount from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    discountv=mycursor.fetchone()
    sellingp=sp.get()
    query="select ex_date from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    date=mycursor.fetchone()
    total=float(quantityv) * float(sellingp)
    # Update the values of the selected item
    if selected_item:
        expiry.item(selected_item, values=(namev, sp.get(), updatequantity.get(),discountv,date,total))
    expiry.selection_remove(expiry.selection())
    
    clear_entryfield() 
      
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

scroll_x=ttk.Scrollbar(outputframe,orient=HORIZONTAL, command=on_vertical_scroll)
scroll_y=ttk.Scrollbar(outputframe,orient=VERTICAL ,command=on_horizontal_scroll)


product_table=ttk.Treeview(outputframe,columns=("whslname","contact","name_of_product","exdate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x=ttk.Scrollbar(command=product_table.xview)
scroll_y=ttk.Scrollbar(command=product_table.yview)

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