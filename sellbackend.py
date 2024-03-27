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
mwindow.title=('Billing')
mwindow.geometry('1440x750+50+20')
# bgOriginal = Image.open('new1.png').resize((1440,750))
#         # bgImage = ImageTk.PhotoImage(bgOriginal)
#         # bgLabel=Label(fwindow,image=bgImage)
#         # bgLabel.place(x=0,y=0)
# img =ImageTk.PhotoImage(bgOriginal)

bgOriginal = Image.open('newbg.png').resize((1500,750))
img =ImageTk.PhotoImage(bgOriginal)
Label(mwindow,image=img,border=0,bg='white').place(x=0,y=0)


def merge_billing_data():
    merged_data = {}
    for item in billing_table.get_children():
        values = billing_table.item(item, 'values')
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
    for item in billing_table.get_children():
        billing_table.delete(item)
    # Insert merged data into billing table
    for data in merged_data.values():
        billing_table.insert('', 'end', values=(
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
    if not billing_table.get_children():
        messagebox.showerror("ERROR",'Billing Table Empty')
        return
    if c_contacte.get()=='' or c_namee.get()=="":
        messagebox.showerror("Error",'Please Enter The Name and Contact of the Customer')
        return
    try:
        query="INSERT INTO graph (date,profit,loss,nos) VALUES (CURDATE(),0.0,0.0,0)"
        mycursor.execute(query)
    except:
        messagebox.showinfo("INFO",'Press OK to Confirm')
    
    for row in billing_table.get_children():
        # Extract data from the treeview
        name_of_product = billing_table.item(row)['values'][0]
        
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
        
        quantity = billing_table.item(row)['values'][2]
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
    for item in billing_table.get_children():
        billing_table.delete(item)
    
def delete_details():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    # Get the currently selected item
    selected_item = billing_table.focus()
    # Delete the selected item
    if selected_item:
        billing_table.delete(selected_item)
    messagebox.showinfo('Sucsess',' Item DELETED Successfully')

    
def generate_invoice():
    if c_contacte.get()=='' or c_namee.get()=="":
        messagebox.showerror("Error",'Please Enter The Name and Contact of the Customer')
        return
    doc = DocxTemplate("miniproject.docx")
    i_name= c_namee.get()
    i_contact= c_contacte.get()
    data = []
    for item in billing_table.get_children():
        values = billing_table.item(item, 'values')
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
    if name.get()=="" or stotal.get()=="" or sp.get()==""or quan.get()=="" or exd.get()=="":
            messagebox.showerror('ERROR','PLEASE FILL ALL THE FIELD')
            return
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
    for item in billing_table.get_children():
        values = billing_table.item(item, 'values')
        if values[0] == namev:
            # Update quantity and total
            new_quantity = int(values[2]) + int(quantinte)
            if quantint < new_quantity :
                messagebox.showerror('Error','NOT ENOUGH STOCK(REENTER QUANTITY)')
                return
            new_total = float(values[5]) + total
            billing_table.item(item, values=(values[0], values[1], new_quantity, values[3], values[4], new_total))
            break
    else:
        # Insert new row
        billing_table.insert('', 'end', values=(namev, sellingp, quantityv, discountv, date, total))
    # Merge data to combine rows with the same product name
    merge_billing_data()
    # Clear entry fields
    clear_entryfield()
   # billing_table.insert("", "end", values=(namev,sellingp,quantityv,discountv,date,total))
    product_table.selection_remove(product_table.selection())
    messagebox.showinfo('Sucsess',' Item ADDED Successfully')
    
    clear_entryfield()

def search():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    search_term = searche.get()
    if search_term:
        # Clear the current content of the treeview
        query="select name,s_price,quantity,s_total,discount,ex_date from finaldbt"             #
        mycursor.execute(query)
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
        # for row in product_table.get_children():
        #     product_table.delete(row)
        # Execute SQL query to fetch names matching the search term
        mycursor.execute("SELECT name,s_price,quantity,s_total,discount,ex_date FROM finaldbt WHERE name LIKE %s", (f'%{search_term}%',))#
        row=mycursor.fetchall()
        
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
            for i in row:
                product_table.insert("",END,values=i)
            con.commit()
        else:
            messagebox.showerror("INVALID SEARCH","NO ITEM IN INVENTORY")
            searche.delete(0,END)
            query="select name,s_price,quantity,s_total,discount,ex_date from finaldbt"
            mycursor.execute(query)
            row=mycursor.fetchall()
            if len(row)!=0:
                product_table.delete(*product_table.get_children())
                for i in row:
                    product_table.insert("",END,values=i)
                con.commit()
            con.close() 
        
    else:
        
        query="select name,s_price,quantity,s_total,discount,ex_date from finaldbt"#
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
    cursor_row=billing_table.focus()
    content=billing_table.item(cursor_row)
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
    selected_item = billing_table.focus()
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
        billing_table.item(selected_item, values=(namev, sp.get(), updatequantity.get(),discountv,date,total))
    billing_table.selection_remove(billing_table.selection())
    messagebox.showinfo('Sucsess',' Item UPDATED Successfully')
    clear_entryfield() 
    
def deselect(event=None):                   ##addkr
    selected_item = product_table.selection()
    if selected_item:
        product_table.selection_remove(selected_item)
        

def on_click_outside(event):
    # Check if the click occurred outside of the treeview
    if event.widget != product_table:
        deselect()
        
mwindow.bind("<Button-1>", on_click_outside)


    
head=Label(mwindow,text="BILLING SECTION")
head.place(x=720,y=0)
head1=Label(mwindow,text="SELECT PRODUCTS TO BE SOLD")
head1.place(x=100,y=30)
outputframe=Frame(mwindow,bd=10,relief=RIDGE)
outputframe.place(x=20,y=50,width=1400,height=200)
head2=Label(mwindow,text="SEARCH : ")
head2.place(x=20,y=265)
searche = Entry(mwindow,width=48,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
searche.place(x=100,y=265)
searchb=Button(mwindow,width=10,text='SEARCH',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=search)
searchb.place(x=500,y=265)

outputframe1=Frame(mwindow,bd=10,relief=GROOVE)
outputframe1.place(x=700,y=265,width=600,height=100)
outputframe2=Frame(mwindow,bd=10,relief=RIDGE)
outputframe2.place(x=20,y=400,width=1400,height=200)
outputframe3=Frame(mwindow,bd=4,relief=RIDGE,pady=6)
outputframe3.place(x=800,y=620,height=80,width=400)

c_namel=Label(outputframe3,text='Name of customer:',bd=0)
c_namel.grid(row=0,column=0,padx=20)
c_namee = Entry(outputframe3,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
c_namee.grid(row=0,column=1)

c_contactl=Label(outputframe3,text='Customer contact:',bd=0)
c_contactl.grid(row=1,column=0,padx=20)
c_contacte = Entry(outputframe3,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
c_contacte.grid(row=1,column=1)

product_table=ttk.Treeview(outputframe,columns=("name_of_product","sellingprice","quantity","sellingpricetotal","discount","exdate"))
vsbp = ttk.Scrollbar(outputframe, orient="vertical", command=product_table.yview)
vsbp.pack(side="right", fill="y")
product_table.configure(yscrollcommand=vsbp.set)

hsbp = ttk.Scrollbar(outputframe, orient="horizontal", command=product_table.xview)
hsbp.pack(side="bottom", fill="x")
product_table.configure(xscrollcommand=hsbp.set)

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

lb=Label(outputframe1,text='Name of product:',bd=0)
lb.grid(row=0,column=0,padx=20)
name = Entry(outputframe1,width=15,fg='black',border=2,bg="white",textvariable=1,font=('Microsoft Yahei UI',10))
name.grid(row=0,column=1)

lb1=Label(outputframe1,text='Quantity:')
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

add=Button(outputframe1,width=10,padx=12,pady=0,text='ADD',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=add_details)
add.place(x=300,y=52)
clear=Button(outputframe1,width=10,padx=12,pady=0,text='CLEAR',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=clear_entryfield)
clear.place(x=420,y=52)

update=Button(mwindow,width=15,pady=7,text='UPDATE',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=update_details)
update.place(x=50,y=610)
updatequantity=Entry(mwindow,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
updatequantity.place(x=180,y=620)

delete=Button(mwindow,width=15,pady=7,text='delete',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=delete_details)
delete.place(x=425,y=610)

print=Button(mwindow,width=15,pady=7,text='print',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=generate_invoice)
print.place(x=1237,y=630)

billing_table=ttk.Treeview(outputframe2,columns=("name_of_product","sellingprice","quantity","discount","exdate","total"))

vsbb = ttk.Scrollbar(outputframe2, orient="vertical", command=billing_table.yview)
vsbb.pack(side="right", fill="y")
billing_table.configure(yscrollcommand=vsbb.set)

hsbb = ttk.Scrollbar(outputframe2, orient="horizontal", command=billing_table.xview)
hsbb.pack(side="bottom", fill="x")
billing_table.configure(xscrollcommand=hsbb.set)

billing_table.heading("name_of_product",text="PRODUCT")
billing_table.heading("sellingprice",text="SELLING PRICE")
billing_table.heading("quantity",text="QUANTITY") 
billing_table.heading("total",text="TOTAL") 
billing_table.heading("discount",text="DISCOUNT") 
billing_table.heading("exdate",text="EXPIRY DATE") 

billing_table["show"]="headings"
billing_table.column("name_of_product",width=100)
billing_table.column("sellingprice",width=75)
billing_table.column("quantity",width=50)
billing_table.column("total",width=75)
billing_table.column("discount",width=50)
billing_table.column("exdate",width=75)
billing_table.pack(fill=BOTH,expand=1)

billing_table.bind("<ButtonRelease-1>",get_cursor2)
fetch_data()

sell=Button(mwindow,width=15,pady=7,text='sell',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=sell_detail)
sell.place(x=1237,y=670)

mwindow.mainloop()
