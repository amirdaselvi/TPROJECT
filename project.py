def details():
    name='EVERGREEN GROCERIES'
    a=name.center(150)
    print(a)
    adrs='Address : West end avenue at west street on man hattans prestigious upper west side'
    b=adrs.center(100)
    print(b)
    Num='CONTACTNO:9852340211'
    c=Num.center(30)
    print(c)
    print("""===================================================================
      ================================================================""")
details()


def add_product():
    #this function is to add the details of product
    #if exist, product can be updated
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the product code:")
    mycursor.execute("SELECT * FROM product WHERE pcode='" + code + "'")    
    records= mycursor.fetchall()
    print(records)
    a=len(records)
    print("Total rows are:  ", a)
    name=input("enter the name of the product:")
    Qty=int(input("enter the quantity of product:"))
    rate =int(input("enter the price of the product:"))
    measure=input("enter the measurement of the quantity:")
    info=(code, name,Qty,rate,measure )
    query="select*from product"
    mycursor.execute(query)
    b=mycursor.fetchall()
    print(b)
    
  
    if a > 0:
       n=input("enter YES or NO to update a product:")
       if n.upper()=="YES":
            for j in records:
                    if j[0]==info[0]:
                        print("enter loop2=====")
                        print (Qty)
                        query1="update product set qty='{}',measurement='{}',rate='{}' Where pcode='{}'".format(j[2]+Qty,measure,rate,j[0])
                        print(query1)
                        mycursor.execute(query1)
                        mycon.commit()
                        print("qty is updated")
                    else:
                        
                       print ("No record matched")
            else:
                print("input not valid")      
 
    else:
        query2="insert into product values('{0}','{1}','{2}','{3}','{4}')".format(code,name,Qty,rate,measure)
        mycursor.execute(query2)
        mycon.commit()
        print("a new product is added")
    print("""===================================================================
      ================================================================""")
def add_supplier():
    #this function is to add the details of supplier
    #if exist, supplier can be updated
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    scode=input("enter the supplier code:")
    mycursor.execute("SELECT * FROM supplier WHERE supcode=" + scode + "")    
    records= mycursor.fetchall()
    a=len(records)
    print("Total rows are:  ", a)
    sname=input("enter the supplier name :")
    address=(input("enter the supplier address:"))
    Num=int(input("enter the supplier phone no:"))
    info=(scode,sname, address,Num)
    query="select*from supplier"
    mycursor.execute(query)
    b=mycursor.fetchall()
    print(b)
    print("welcome1")
    print(a)
    x=int(scode)
    y=int(b[0][0])
    if a > 0:
        
        n=input("enter YES or NO to update a product:")
        if n.upper()=="YES":
            for j in records:
                    print("enter loop2=====")
                    print(x)
                    print(y)
                    if y==x:
                         print("enter loop2=====")
                         query1="update supplier set address='{}'where supcode='{}'".format(address,scode)
                         print(query1)
                         mycursor.execute(query1)
                         mycon.commit()
                         print("address and scode updated")
                    else:
                       print ("No record matched")
            else:
               print("input not valid")      

    else:
         query2="insert into supplier values('{0}','{1}','{2}','{3}')".format(scode,sname,address,Num)
         mycursor.execute(query2)
         mycon.commit()
         print("a new supplier is added")
    print("""===================================================================
      ================================================================""")

def add_customer():
    #this function is to add the details of customer
    #if exist, customer can be updated
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the customer code:")
    mycursor.execute("SELECT * FROM customer WHERE cuscode=" + code + "")    
    records= mycursor.fetchall()
    a=len(records)
    print("Total rows are:  ", a)
    name=input("enter the customer name :")
    address=(input("enter the customer address:"))
    Num=int(input("enter the customer phone no:"))
    info=(code,name, address,Num)
    query="select*from customer"
    mycursor.execute(query)
    b=mycursor.fetchall()
    print(b)
    print("welcome1")
    print(a)
    x=int(code)
    y=int(b[0][0])
    if a > 0:
        
        n=input("enter YES or NO to update a product:")
        if n.upper()=="YES":
            for j in records:
                    print("enter loop2=====")
                    print(x)
                    print(y)
                    if y==x:
                         print("enter loop2=====")
                         query1="update customer set address='{}'where cuscode='{}'".format(address,code)
                         print(query1)
                         mycursor.execute(query1)
                         mycon.commit()
                         print("address is updated")
                    else:
                       print ("No record matched")
            else:
               print("input not valid")      

    else:
         query2="insert into customer values('{0}','{1}','{2}','{3}')".format(code,name,address,Num)
         mycursor.execute(query2)
         mycon.commit()
         print("a new customer is added")
    print("""===================================================================
      ================================================================""")

def add_Employee():
    #this function is to add the details of Employee
    #if exist, Employee can be updated
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the Employee code:")
    mycursor.execute("SELECT * FROM Employee  WHERE Ecode='" + code + "'")    
    records= mycursor.fetchall()
    print(records)
    a=len(records)
    print("Total rows are:  ", a)
    name=input("enter the name of the employee:")
    num=int(input("enter the contact number of the employee:"))
    address =input("enter the address of the employee:")
    date=input("enter the date of join of the employee:")
    sal=int(input("enter the salary of the emplyoee:"))
    info=(code, name,num,address,date ,sal)
    query="select*from employee"
    mycursor.execute(query)
    b=mycursor.fetchall()
    print(b)
    print("welcome1")
    print(a)
  
    if a > 0:
       n=input("enter YES or NO to update a employee:")
       if n.upper()=="YES":
            for j in records:
                   if j[0]==info[0]:
                        print (salary)
                        query1="update product set salary='{}',Enum='{}',Address='{}' Where Ecode='{}'".format(j[5]+sal,num,address,j[0])
                        print(query1)
                        mycursor.execute(query1)
                        mycon.commit()
                        print("salary is updated")
               #else:
                 #print ("No record matched")
            else:  
                print("input not valid")      
 
    else:
        query2="insert into Employee values('{0}','{1}','{2}','{3}','{4}','{5}')".format(code,name,num,address,date,sal)
        mycursor.execute(query2)
        mycon.commit()
        print("a new employee is added")
    print("""===================================================================
      ================================================================""")
    

def delete_product():
    #this function is to delete a product
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the product code to be deleted:")
    query="delete from product where pcode='{}'".format(code)
    print(query)
    mycursor.execute(query)
    mycon.commit()
    print("the product is deleted")
    print("""===================================================================
      ================================================================""")

def delete_supplier():
    #this function is to delete a supplier
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the supplier code to be deleted:")
    query="delete from supplier where supcode='{}'".format(code)
    print(query)
    mycursor.execute(query)
    mycon.commit()
    print("the supplier is deleted")
    print("""===================================================================
      ================================================================""")

def delete_customer():
    #this function is to delete a customer
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the customer code to be deleted:")
    query="delete from customer where cuscode='{}'".format(code)
    print(query)
    mycursor.execute(query)
    mycon.commit()
    print("the customerr is deleted")
    print("""===================================================================
      ================================================================""")

def delete_Employee():
    #this function is to delete a employee
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the Employee code to be deleted:")
    query="delete from Employee where Ecode='{}'".format(code)
    print(query)
    mycursor.execute(query)
    mycon.commit()
    print("the Employee is deleted")
    print("""===================================================================
      ================================================================""")

def search_product():
    #this function is to search a product
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the product code:")
    mycursor.execute("SELECT * FROM product WHERE pcode='" + code + "'")    
    r= mycursor.fetchone()
    a=len(r)
    print("Total rows are:  ", a)
    print(r)
   
    if a>0:
       print("the product name is :",r[1])
       print("the quantity is :",r[2])
       print("the rate is:",r[3])
       print("the measurment is:",r[4])
       
    else:
        print("No record is found")
    print("""===================================================================
      ================================================================""")
    

def search_supplier():
     #this function is to search a supplier
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the supplier code:")
    mycursor.execute("SELECT * FROM Supplier WHERE supcode='" + code + "'")    
    r= mycursor.fetchone()
    a=len(r)
    print("Total rows are:  ", a)
    print(r)
   
    if a>0:
       print("the supplier name is :",r[1])
       print("the address is :",r[2])
       print("the number is:",r[3])
       
       
    else:
        print("No record is found")
    print("""===================================================================
      ================================================================""")

def search_customer():
     #this function is to search a customer
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the customer code:")
    mycursor.execute("SELECT * FROM customer WHERE cuscode='" + code + "'")    
    r= mycursor.fetchone()
    a=len(r)
    print("Total rows are:  ", a)
    print(r)
    if a>0:
       print("the customer name is :",r[1])
       print("the address is :",r[2])
       print("the phone no is:",r[3])
       
    else:
        print("No record is found")
    print("""===================================================================
      ================================================================""")


def search_Employee():
     #this function is to search a employee
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    code=input("enter the employee code:")
    mycursor.execute("SELECT * FROM Employee WHERE Ecode='" + code + "'")    
    r= mycursor.fetchone()
    a=len(r)
    print("Total rows are:  ", a)
    print(r)
   
    if a>0:
       print("the Employee name is :",r[1])
       print("employee no is :",r[2])
       print("address is:",r[3])
       print("the date of join is:",r[4])
       print("salary is:",r[5])
       
       
    else:
        print("No record is found")
    print("""===================================================================
      ================================================================""")


def inv_detail ():
    #this function is to add the details of invdetail and invheader
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor=mycon.cursor()
    invno=int(input("Enter the invoice number:"))
    invdate=str(input("enter the date:"))
    strcusname=input("enter the  customer name:")
    cusadd= (input("enter the customer address:"))
    invamt=0
    query = "insert into invheader values('{0}','{1}','{2}','{3}','{4}')".format(invno,invdate,strcusname,cusadd,invamt )
    mycursor.execute(query)
    mycon.commit()
    print("added")
    flag=input("Enter yes or no to add item:")
    
    mycon1=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
    mycursor2=mycon1.cursor()
    i=0
    while flag.upper()=="YES":
        i+=1
        code=input("enter the product code:")
        mycursor2.execute("SELECT * FROM product WHERE pcode='" + code + "'")    
        records= mycursor2.fetchall()
        print(records)
        pname=records[0][1]
        print("The product name is ",pname)
        qty=int(input("enter the quantity of the product:"))
        unt=records[0][4]
        print("The unit of the product is ",unt)
        rate=records[0][3]
        print("The rate of the product is ",rate)
        total=qty*rate
        print(total)
        invamt+=total
        print(invamt)
        query1= "insert into invdetail values('{0}','{1}','{2}','{3}','{4}','{5}')".format(invno,i,pname,qty,unt,total )
        print(query1)
        mycursor2.execute(query1)
        mycon1.commit()
        flag=input("Enter yes or no to add item:")

    query2="update invheader set invamount='{}' Where Invno='{}'".format(invamt,invno)
    mycursor2.execute(query2)
    print("updated")
    mycon1.commit()
    print("""===================================================================
      ================================================================""")
                    

def rec():
    
    #this function is to generate bill
    import csv
    f=open("bill.csv","w",newline='')
    a=csv.writer(f)
    l=[]
    a.writerow(["pname","qty","unit","price"])
    while True:
        import mysql.connector
        mycon=mysql.connector.connect(host="localhost",user="root",password="amirda@123",database="project")
        mycursor=mycon.cursor()
        b= input ("enter pcode to get the details")
        print("select * from product where pcode=", b)
        mycursor.execute("select * from product where pcode='" + b+"'")
        r= mycursor.fetchall()
        print(r)
    
        
        pname=r[0][1]
        qty=r[0][2]
        unit=r[0][3]
        price=r[0][4]
        a.writerow([pname,qty, unit,price])
        print("record inserted")
        ch=input("enter yes or no to continue:")
        if ch=="no":
                        break

    mycon.commit()
    f.close()
    print("""===================================================================
      ================================================================""")
                        
while True:
        print("1)To add products")
        print("2)To add suppliers")
        print("3)To add customers")
        print("4)To add employee")
        print("5)To delete products")
        print("6)To delete supplier")
        print("7)To delete customer")
        print("8)To delete employee")
        print("9)To search product")
        print("10)To search supplier")
        print("11)To search customer")
        print("12)To search Employee")
        print("13)Invdetail and Invheader")
        print("14)To generate bill")
        choice=int(input("Enter your choice"))
        if choice == 1:
            print("calling add")
            add_product()
        elif choice==2:
            add_supplier()
        elif choice==3:
            add_customer()
        elif choice==4:
            add_Employee()
        elif choice==5:
            delete_product()
        elif choice==6:
            delete_supplier()
        elif choice==7:
            delete_customer()
        elif choice==8:
            delete_Employee()
        elif choice==9:
            search_product()
        elif choice==10:
            search_supplier()
        elif choice==11:
            search_customer()
        elif choice==12:
            search_Employee()
        elif choice==13:
            inv_detail()
        elif choice==14:
            rec()
        elif choice==15:
          print("exit")
          break

from tkinter import *
window = Tk()
#===================================VARIABLE=================================
from tkinter import messagebox
c_name=StringVar()
cgst=StringVar()
inv_no=StringVar()
ph_no=StringVar()
item=StringVar()
Rate=IntVar()
qty=IntVar()
bill_no=IntVar()
global l
l=[]
#===================================FUNCTION=========================================
def wlcm():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t\t\tEVERGREEN GROCERRIES")
    textarea.insert(END,"\n No.123,Lawrence road,Kodambakkam,Chennai-600 024")
    textarea.insert(END,"\tGSTIN : 37AADCS0472N1Z1")
    textarea.insert(END,f'\nInvoice No. :\t\t{inv_no.get()}')
    textarea.insert(END,f'\nCustomer Name. :\t\t{c_name.get()}')
    textarea.insert(END,f'\nGSTIN :\t\t{cgst.get()}')
    textarea.insert(END,f'\nPhone no :\t\t{ph_no.get()}')
    textarea.insert(END,f'\n=========================================================================')
    textarea.insert(END,f'\n\t\t Product\t\t\t QTY\t\t Price')
    textarea.insert(END,f'\n=========================================================================')
    textarea.configure(font=('Segoe Print', 10, 'bold'))

def additm():
    n=Rate.get()
    m=qty.get()*n
    l.append(m)
    if item.get()==' ':
        messagebox.showerror("Error","Please Enter the item")
    else:
        textarea.insert(END,f'\n\t\t{item.get()}\t\t\t{qty.get()}\t\t{m}')

def gbill():
    if c_name.get()=='' or ph_no.get=='':
        messagebox.showerror('ERROR','Customer name is must')
    else:
        tex=textarea.get(10.0,(10.0+float(len(l))))
        wlcm()
        textarea.insert(END,tex)
        textarea.insert(END,f'\n=========================================================================')
        textarea.insert(END,f'Total :\t\t\t\t\t\t\t{sum(l)}')
        textarea.insert(END,f'\n=========================================================================')
        savebill()
def savebill():
    op=messagebox.askyesno("Save bill",'Do you want to save the bill')
    if op>0:
        bill_details=textarea.get(1.0,END)
        f1=open("bills/"+str(bill_no.get())+".txt",'w')
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo('Saved',f'Bill no:{bill_no.get()} Saved succesfully')
    else:
        return
def clear():
    c_name.set(' ')
    ph_no.set(' ')
    item.set(' ')
    Rate.set(0)
    qty.set(0)
    wlcm()
    
def back():
    op=messagebox.askyesno('Exit','Do you really want to exit')
    if op>0:
        window.destroy()
        
#===================================TOP SECTION==================================================================================================
l1 = Label(window, text="EVERGREEN GROCERRIES",bg="#29CDA8",fg="black",font=("Segoe Print",33,'bold'),width="300",height="2").pack()
l1_txt=Label(window,text="No.123,Lawrence road,Kodambakkam,Chennai-600 024",bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="50",height="1")
l12_txt=Label(window,text="GSTIN : 37AADCS0472N1Z1",bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="25",height="1")
l12_txt.place(x=1150,y=100)
l1_txt.place(x=435,y=100)
window.geometry("500x500")

#=================================================CUSTOMER DETAILS==============================================================================
#2
l3=LabelFrame(window,text="Invoice No.",bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width='200',height='90',relief=SUNKEN)
l3.place(x=0,y=250)
l3_txt=Entry(l3,width=18,font=("Segoe Print",15,'bold'),relief=SUNKEN,textvariable=inv_no )
l3_txt.grid(row=0,column=0,padx=10,pady=5)

#1
l2=LabelFrame(window,text="Date",bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="100",height="90",relief=SUNKEN)
l2.place(x=0,y=163)
l2_txt=Entry(l2,width=18,font=("Segoe Print",15,'bold'),relief=SUNKEN)
l2_txt.grid(row=0,column=0,padx=10,pady=5)

#3
customer=LabelFrame(window,text="Bill To:",bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="100",height="90",relief=SUNKEN)
customer.place(x=0,y=330)
cust=Entry(customer,width=18,font=("Segoe Print",15,'bold'),relief=SUNKEN,textvariable=c_name)
cust.grid(row=0,column=1,padx=10,pady=5)

#4
gst=LabelFrame(window,text="GSTIN",bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="100",height="90",relief=SUNKEN)
gst.place(x=0,y=420)
gst_txt=Entry(gst,width=18,font=("Segoe Print",15,'bold'),relief=SUNKEN,textvariable=cgst)
gst_txt.grid(row=0,column=0,padx=10,pady=5)

#5
ph=LabelFrame(window,text="Phone No.",bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="100",height="90",relief=SUNKEN)
ph.place(x=0,y=500)
phno=Entry(ph,width=18,font=("Segoe Print",15,'bold'),relief=SUNKEN,textvariable=ph_no)
phno.grid(row=1,column=3,padx=10,pady=5)

#==================================================================PRODUCT DETAILS==============================================================
product=LabelFrame(window,text="Product details",bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="100",height="90",relief=SUNKEN)
product.place(x=295,y=150,width=600,height=500)

itm=LabelFrame(product,text='Product name',bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="100",height="90",relief=SUNKEN)
itm.place(x=0,y=10)
itm_txt=Entry(itm,width=18,font=("Segoe Print",15,'bold'),relief=SUNKEN,textvariable=item)
itm_txt.grid(row=0,column=0,padx=30,pady=20)

rate=LabelFrame(product,text='Product rate',bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="100",height="90",relief=SUNKEN)
rate.place(x=0,y=150)
rate_txt=Entry(rate,width=18,font=("Segoe Print",15,'bold'),relief=SUNKEN,textvariable=Rate)
rate_txt.grid(row=0,column=0,padx=30,pady=20)

qut=LabelFrame(product,text='Quantity',bg="#29CDA8",fg="black",font=("Segoe Print",15,'bold'),width="40",height="90",relief=SUNKEN)
qut.place(x=0,y=300)
qut_txt=Entry(qut,width=18,font=("Segoe Print",15,'bold'),relief=SUNKEN,textvariable=qty)
qut_txt.grid(row=0,column=0,padx=30,pady=20)

#======================================================BUTTONS==================================================================================

btn1=Button(product,text='Add Item',bg="#3A29CD",fg="white",font=("Segoe Print",15,'bold'),command=additm)
btn1.grid(row=1,column=10,padx=400,pady=30)

btn2=Button(product,text='Generate Bill',bg="#3A29CD",fg="white",font=("Segoe Print",15,'bold'),command=gbill)
btn2.grid(row=2,column=10,padx=400,pady=20)

btn3=Button(product,text='Clear',bg="#3A29CD",fg="white",font=("Segoe Print",15,'bold'),command=clear)
btn3.grid(row=3,column=10,padx=400,pady=20)

btn4=Button(product,text='Exit',bg="#3A29CD",fg="white",font=("Segoe Print",15,'bold'),command=back)
btn4.grid(row=4,column=10,padx=450,pady=20)

#===========================================BILL AREA============================================================================================
F=Frame(window,relief=GROOVE,bd=10)
F.place(x=850,y=130,width=600,height=620)

bill_title=Label(F,text='Tax Invoice',bg="#29CDA8",fg="black",font=("Segoe Print",20,'bold'),relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F,orient=VERTICAL)
textarea=Text(F,y=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
wlcm()
print("""===================================================================
      ================================================================""")
print("Thankyou for comming. Visit again!")
    

    
    


    
    
