from tkinter import *
from tkinter import messagebox
import mysql.connector
#================
window=Tk()      

class LoginStatus:
 loginStatus=0
 loginUsername="Null"
#================
def homeframeEvent(event):
 loginframe.pack_forget()
 registerframe.pack_forget()
 physiotherapyframe.pack_forget()
 exerciseframe.pack_forget()
 PhysioPrd1frame.pack_forget()
 PhysioPrd2frame.pack_forget()
 PhysioPrd3frame.pack_forget()
 PhysioPrd4frame.pack_forget()
 PhysioPrd5frame.pack_forget()
 PhysioPrd6frame.pack_forget()
 ExercisePrd1frame.pack_forget()
 ExercisePrd2frame.pack_forget()
 ExercisePrd3frame.pack_forget()
 ExercisePrd4frame.pack_forget()
 ExercisePrd5frame.pack_forget()
 ExercisePrd6frame.pack_forget()
 homeframe.pack()

def loginframeEvent(event):
 homeframe.pack_forget()
 registerframe.pack_forget()
 physiotherapyframe.pack_forget()
 exerciseframe.pack_forget()
 PhysioPrd1frame.pack_forget()
 PhysioPrd2frame.pack_forget()
 PhysioPrd3frame.pack_forget()
 PhysioPrd4frame.pack_forget()
 PhysioPrd5frame.pack_forget()
 PhysioPrd6frame.pack_forget()
 ExercisePrd1frame.pack_forget()
 ExercisePrd2frame.pack_forget()
 ExercisePrd3frame.pack_forget()
 ExercisePrd4frame.pack_forget()
 ExercisePrd5frame.pack_forget()
 ExercisePrd6frame.pack_forget() 
 loginframe.pack()
 
def registerframeEvent(event):
 homeframe.pack_forget()
 loginframe.pack_forget()
 physiotherapyframe.pack_forget()
 exerciseframe.pack_forget()
 PhysioPrd1frame.pack_forget()
 PhysioPrd2frame.pack_forget()
 PhysioPrd3frame.pack_forget()
 PhysioPrd4frame.pack_forget()
 PhysioPrd5frame.pack_forget()
 PhysioPrd6frame.pack_forget()
 ExercisePrd1frame.pack_forget()
 ExercisePrd2frame.pack_forget()
 ExercisePrd3frame.pack_forget()
 ExercisePrd4frame.pack_forget()
 ExercisePrd5frame.pack_forget()
 ExercisePrd6frame.pack_forget()
 registerframe.pack()

def physiotherapyframeEvent(event):
 homeframe.pack_forget()
 loginframe.pack_forget()
 registerframe.pack_forget()
 exerciseframe.pack_forget()
 PhysioPrd1frame.pack_forget()
 PhysioPrd2frame.pack_forget()
 PhysioPrd3frame.pack_forget()
 PhysioPrd4frame.pack_forget()
 PhysioPrd5frame.pack_forget()
 PhysioPrd6frame.pack_forget()
 ExercisePrd1frame.pack_forget()
 ExercisePrd2frame.pack_forget()
 ExercisePrd3frame.pack_forget()
 ExercisePrd4frame.pack_forget()
 ExercisePrd5frame.pack_forget()
 ExercisePrd6frame.pack_forget()
 physiotherapyframe.pack()

def exerciseframeEvent(event):
 homeframe.pack_forget()
 loginframe.pack_forget()
 registerframe.pack_forget()
 physiotherapyframe.pack_forget()
 PhysioPrd1frame.pack_forget()
 PhysioPrd2frame.pack_forget()
 PhysioPrd3frame.pack_forget()
 PhysioPrd4frame.pack_forget()
 PhysioPrd5frame.pack_forget()
 PhysioPrd6frame.pack_forget()
 ExercisePrd1frame.pack_forget()
 ExercisePrd2frame.pack_forget()
 ExercisePrd3frame.pack_forget()
 ExercisePrd4frame.pack_forget()
 ExercisePrd5frame.pack_forget()
 ExercisePrd6frame.pack_forget()
 exerciseframe.pack()

def PhysioPrd1Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  PhysioPrd1frame.pack()

def PhysioPrd2Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget()
  PhysioPrd1frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  PhysioPrd2frame.pack()

def PhysioPrd3Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget()
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  PhysioPrd3frame.pack()
 
def PhysioPrd4Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget()
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  PhysioPrd4frame.pack()

def PhysioPrd5Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget()
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  PhysioPrd5frame.pack()

def PhysioPrd6Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget()
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  PhysioPrd6frame.pack()

def ExercisePrd1Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget()
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  ExercisePrd1frame.pack()

def ExercisePrd2Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget()
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  ExercisePrd2frame.pack()

def ExercisePrd3Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget() 
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  ExercisePrd3frame.pack()

def ExercisePrd4Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget() 
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  ExercisePrd4frame.pack()

def ExercisePrd5Event(event):
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget() 
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd6frame.pack_forget()
  ExercisePrd5frame.pack()
 
def ExercisePrd6Event(event): 
  homeframe.pack_forget()
  loginframe.pack_forget()
  registerframe.pack_forget()
  physiotherapyframe.pack_forget()
  exerciseframe.pack_forget() 
  PhysioPrd1frame.pack_forget()
  PhysioPrd2frame.pack_forget()
  PhysioPrd3frame.pack_forget()
  PhysioPrd4frame.pack_forget()
  PhysioPrd5frame.pack_forget()
  PhysioPrd6frame.pack_forget()
  ExercisePrd1frame.pack_forget()
  ExercisePrd2frame.pack_forget()
  ExercisePrd3frame.pack_forget()
  ExercisePrd4frame.pack_forget()
  ExercisePrd5frame.pack_forget()
  ExercisePrd6frame.pack()

def SetEditableFalse():
  DisplayBill_User_fname_txt.config(state=DISABLED)
  DisplayBill_User_lname_txt.config(state=DISABLED)
  DisplayBill_User_uname_txt.config(state=DISABLED)
  DisplayBill_User_pincode_txt.config(state=DISABLED)
  DisplayBill_User_address_txt.config(state=DISABLED)

  DisplayBill_Delivery_fname_txt.config(state=DISABLED)
  DisplayBill_Delivery_lname_txt.config(state=DISABLED)
  DisplayBill_Delivery_prdname_txt.config(state=DISABLED)
  DisplayBill_Delivery_deliverydate_txt.config(state=DISABLED)
  DisplayBill_Delivery_pincode_txt.config(state=DISABLED)
  DisplayBill_Delivery_address_txt.config(state=DISABLED)

  DisplayBill_ProductDetails_prdname_txt.config(state=DISABLED)
  DisplayBill_ProductDetails_quantity_txt.config(state=DISABLED)
  DisplayBill_ProductDetails_purchasetype_txt.config(state=DISABLED)
  DisplayBill_ProductDetails_prdprice_txt.config(state=DISABLED)
          
  DisplayBill_PricingDetails_quantity_txt.config(state=DISABLED)
  DisplayBill_PricingDetails_productprice_txt.config(state=DISABLED)
  DisplayBill_PricingDetails_totalprice_txt.config(state=DISABLED)

def SetEditableTrue():
  DisplayBill_User_fname_txt.config(state=NORMAL)
  DisplayBill_User_lname_txt.config(state=NORMAL)
  DisplayBill_User_uname_txt.config(state=NORMAL)
  DisplayBill_User_pincode_txt.config(state=NORMAL)
  DisplayBill_User_address_txt.config(state=NORMAL)

  DisplayBill_Delivery_fname_txt.config(state=NORMAL)
  DisplayBill_Delivery_lname_txt.config(state=NORMAL)
  DisplayBill_Delivery_prdname_txt.config(state=NORMAL)
  DisplayBill_Delivery_deliverydate_txt.config(state=NORMAL)
  DisplayBill_Delivery_pincode_txt.config(state=NORMAL)
  DisplayBill_Delivery_address_txt.config(state=NORMAL)

  DisplayBill_ProductDetails_prdname_txt.config(state=NORMAL)
  DisplayBill_ProductDetails_quantity_txt.config(state=NORMAL)
  DisplayBill_ProductDetails_purchasetype_txt.config(state=NORMAL)
  DisplayBill_ProductDetails_prdprice_txt.config(state=NORMAL)
          
  DisplayBill_PricingDetails_quantity_txt.config(state=NORMAL)
  DisplayBill_PricingDetails_productprice_txt.config(state=NORMAL)
  DisplayBill_PricingDetails_totalprice_txt.config(state=NORMAL)

def DisplayBillDetails(name,purchasetype,qty,price,result):
  try:
    con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")

    DisplayBill_User_fname_txt.insert(0,result[0][1])
    DisplayBill_User_lname_txt.insert(0,result[0][2])
    DisplayBill_User_uname_txt.insert(0,result[0][3])
    DisplayBill_User_pincode_txt.insert(0,str(result[0][5]))
    DisplayBill_User_address_txt.insert(0,result[0][6])
     
    DisplayBill_Delivery_fname_txt.insert(0,result[0][1])
    DisplayBill_Delivery_lname_txt.insert(0,result[0][2])
    DisplayBill_Delivery_prdname_txt.insert(0,name)
    DisplayBill_Delivery_deliverydate_txt.insert(0,"2 days after purchasing")
    DisplayBill_Delivery_pincode_txt.insert(0,str(result[0][5]))
    DisplayBill_Delivery_address_txt.insert(0,result[0][6]) 
    
    DisplayBill_ProductDetails_prdname_txt.insert(0,name)
    DisplayBill_ProductDetails_quantity_txt.insert(0,qty.get())
    DisplayBill_ProductDetails_purchasetype_txt.insert(0,purchasetype)
    DisplayBill_ProductDetails_prdprice_txt.insert(0,price) 
      
    DisplayBill_PricingDetails_quantity_txt.insert(0,qty.get())
    DisplayBill_PricingDetails_productprice_txt.insert(0,str(price))
    total=price*int(qty.get())
    DisplayBill_PricingDetails_totalprice_txt.insert(0,total) 
    
    cur=con.cursor()

    if purchasetype=="On Leased":
     sql="insert into rent(fname,lname,username,address,pincode,purchase_type,product_name,quantity,product_price,total_price) values('{}','{}','{}','{}',{},'{}','{}',{},{},{});".format(result[0][1],result[0][2],result[0][3],result[0][6],result[0][5],purchasetype,name,int(qty.get()),price,total)
     cur.execute(sql)
     con.commit()
    
    elif purchasetype=="Purchased":
     sql="insert into buy(fname,lname,username,address,pincode,purchase_type,product_name,quantity,product_price,total_price) values('{}','{}','{}','{}',{},'{}','{}',{},{},{});".format(result[0][1],result[0][2],result[0][3],result[0][6],result[0][5],purchasetype,name,int(qty.get()),price,total)
     cur.execute(sql)
     con.commit()
    
    else:
      messagebox.showerror("","Invalid Product Type")

  except:
   messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
   con.rollback()
  
  finally:
    if con:
      con.close()

def ClearBillDetails():

  DisplayBill_User_fname_txt.delete(0,END)
  DisplayBill_User_lname_txt.delete(0,END)
  DisplayBill_User_uname_txt.delete(0,END)
  DisplayBill_User_pincode_txt.delete(0,END)
  DisplayBill_User_address_txt.delete(0,END)

  DisplayBill_Delivery_fname_txt.delete(0,END)
  DisplayBill_Delivery_lname_txt.delete(0,END)
  DisplayBill_Delivery_prdname_txt.delete(0,END)
  DisplayBill_Delivery_deliverydate_txt.delete(0,END)
  DisplayBill_Delivery_pincode_txt.delete(0,END)
  DisplayBill_Delivery_address_txt.delete(0,END)

  DisplayBill_ProductDetails_prdname_txt.delete(0,END)
  DisplayBill_ProductDetails_quantity_txt.delete(0,END)
  DisplayBill_ProductDetails_purchasetype_txt.delete(0,END)
  DisplayBill_ProductDetails_prdprice_txt.delete(0,END)

  DisplayBill_PricingDetails_quantity_txt.delete(0,END)
  DisplayBill_PricingDetails_productprice_txt.delete(0,END)
  DisplayBill_PricingDetails_totalprice_txt.delete(0,END)

def Finish():
  SetEditableTrue()
  ClearBillDetails()
  DisplayBillframe.pack_forget()
  homeframe.pack()

#===============LOGIN FORM
def LoginValidation():
 
 try:
   con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
   cur=con.cursor()
   sql="select password from user where username='{}';".format(login_username_txt.get())
   cur.execute(sql)
   result=cur.fetchall()
   
   if result: 

     if login_password_txt.get()==result[0][0]:
         messagebox.showinfo("Login Button Click","Login Successfull")
         LoginStatus.loginUsername=login_username_txt.get()
         LoginStatus.loginStatus=1
         loginframe.pack_forget()
         homeframe.pack()
         welcome_lbl.config(text="Welcome {}".format(login_username_txt.get()))

     else:
       messagebox.showerror("Login Button Click","Invalid Credentials")
   
   else:
     messagebox.showerror("Login Button Click"," User Not There")
    
 except:
   messagebox.showerror("ODBC Connectivity","ODBC Connection Fail")  
    
 finally:
   if con:
    con.close()

def RegisterLink():
 loginframe.pack_forget()
 registerframe.pack()

def CancleButtonClick():
 loginframe.pack_forget()
 homeframe.pack()

window.resizable(False,False)
loginframe=Frame(window,bg="white",width=443,height=293)

'All Label for Login Frame'
login_title_lbl=Label(loginframe,text="Physio-Equip Surgical",font=("Times new Roman",27,"bold","italic"),fg="purple",bg="white")
login_lbl=Label(loginframe,text="Login Form",font=("SimSun-ExtB",18,"bold"),fg="Red",bg="white")
login_username_lbl=Label(loginframe,text="Username :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white") 
login_password_lbl=Label(loginframe,text="Password :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white")

'All Textfield for Login Frame'
login_username_txt=Entry(loginframe,font=("Calibri",15),bg="lightgrey",bd=2)
login_password_txt=Entry(loginframe,show="\u2022",font=("Calibri",15),bg="lightgrey",bd=2)

'All Button for Login Frame'
login_btn=Button(loginframe,text="Login",font=("Calibri",15),bg="blue",fg="white",cursor="hand2",command=LoginValidation)
login_cancle_btn=Button(loginframe,text="Cancle",font=("Calibri",15),bg="red",fg="white",cursor="hand2",command=CancleButtonClick)
registerLink_btn=Button(loginframe,text="Click here to create a new account",font=("Segoe UI Symbol",12,"bold"),fg="Darkblue",bg="white",bd=0,command=RegisterLink,cursor="hand2")
   
'Using Place layout manager'
login_title_lbl.place(x=48,y=0)
login_lbl.place(x=22,y=80)
login_username_lbl.place(x=100,y=130)
login_password_lbl.place(x=100,y=170)

login_username_txt.place(x=210,y=135,width=120,height=25)
login_password_txt.place(x=210,y=175,width=120,height=25)

login_btn.place(x=250,y=218,height=33,width=74)
login_cancle_btn.place(x=155,y=220,height=30,width=74)
registerLink_btn.place(x=90,y=250,height=35)

'All Labels for Menu Bar'
login_home_lbl=Label(loginframe,text="Home",font=("Tahoma",12,"bold"),fg="hot pink",bg="white",cursor="hand2")
login_login_lbl=Label(loginframe,text="Login",font=("Tahoma",12,"bold"),fg="hot pink",bg="white",cursor="hand2")
login_register_lbl=Label(loginframe,text="Register",font=("Tahoma",12,"bold"),fg="hot pink",bg="white",cursor="hand2")
login_physiotherapy_lbl=Label(loginframe,text="Physiotherapy",font=("Tahoma",12,"bold"),fg="hot pink",bg="white",cursor="hand2")
login_exercise_lbl=Label(loginframe,text="Excercise",font=("Tahoma",12,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
login_home_lbl.place(x=10,y=49)
login_login_lbl.place(x=70,y=49)
login_register_lbl.place(x=130,y=49)
login_physiotherapy_lbl.place(x=210,y=49)
login_exercise_lbl.place(x=336,y=49)

'Applying Events on Labels'
login_home_lbl.bind("<Button-1>",homeframeEvent)
login_login_lbl.bind("<Button-1>",loginframeEvent)
login_register_lbl.bind("<Button-1>",registerframeEvent)
login_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
login_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

#===============HOME PAGE
window.resizable(False,False)
homeframe=Frame(window,bg="white",width=698,height=600)
homeframe.pack()

'All Label for Menu Bar' 
title_lbl=Label(homeframe,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white",cursor="hand2")
home_lbl=Label(homeframe,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
login_lbl=Label(homeframe,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
register_lbl=Label(homeframe,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
physiotherapy_lbl=Label(homeframe,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_lbl=Label(homeframe,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
welcome_lbl=Label(homeframe,font=("Tahoma",20,"bold"),fg="SeaGreen2",text="",bg="white")

img1=PhotoImage(file=r".\Images\intro pic.png")
img2=PhotoImage(file=r".\Images\example for home page.png")
img3=PhotoImage(file=r".\Images\Our Clients.png")
Label(homeframe,bg="white",image=img1).place(x=0,y=140,height=180,width=698)
Label(homeframe,bg="white",image=img2).place(x=0,y=325,height=150,width=698)
Label(homeframe,bg="white",image=img3).place(x=0,y=480,height=115,width=698)

'Using place layout manager'
title_lbl.place(x=140,y=0)
home_lbl.place(x=5,y=60)
login_lbl.place(x=80,y=60)
register_lbl.place(x=155,y=60)
physiotherapy_lbl.place(x=253,y=60)
exercise_lbl.place(x=410,y=60)
welcome_lbl.place(x=5,y=90)

'Applying Events on Labels'
home_lbl.bind("<Button-1>",homeframeEvent)
login_lbl.bind("<Button-1>",loginframeEvent)
register_lbl.bind("<Button-1>",registerframeEvent)
physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
exercise_lbl.bind("<Button-1>",exerciseframeEvent)

#==============REGISTER FORM
def EnterIntoDatabase():  
 fname=register_fname_txt.get()
 lname=register_lname_txt.get()
 uname=register_username_txt.get()
 pas=register_password_txt.get()
 retypePass=register_retypepassword_txt.get()
 pin=register_pincode_txt.get()
 address=register_address_txt.get("1.0",END)

 'Check whether all fields are filled or not'

 if fname=="" or lname=="" and uname=="" or pas=="" and pin=="" or address=="":
   messagebox.showerror("Register Button Click","Fill All Details") 

 elif pas != retypePass:
   messagebox.showerror("Register Button Click","Password And RetypePassword Doesn't Match")

 else: 
  
  try:
    con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
    cur=con.cursor()
    sql="select username from user where username='{}';".format(uname)
    cur.execute(sql)
    result=cur.fetchall()
    
    if result:
      
      'No Repetetion of Username by any user'

      if result[0][0]==uname:
       messagebox.showerror("Register Button Click","User Name Already Exisits")
    
    else:
        sql="insert into user(fname,lname,username,password,pincode,address) values('{}','{}','{}','{}',{},'{}');".format(fname,lname,uname,pas,int(pin),address)
        cur.execute(sql)
        con.commit()
        messagebox.showinfo("Register Button Click","User Register Successfully\n{} Rows Inserted in Physio-Equip Database".format(cur.rowcount))
        registerframe.pack_forget()
        loginframe.pack()
    
  except:
    messagebox.showerror("ODBC Connectivity","ODBC Connection Fail")  
    con.rollback()
    
  finally:
    if con:
     con.close()

def RegisterCancleButtonClick():
  print("Register Cancle Button Clicked")
  registerframe.pack_forget()
  homeframe.pack()

def LoginLink():
 print("Login Link Button Clicked!!")
 registerframe.pack_forget()
 loginframe.pack()

window.resizable(False,False)
registerframe=Frame(window,bg="white",width=698,height=600)

'All Label for register frame'
register_title_lbl=Label(registerframe,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
register_lbl=Label(registerframe,text="Registration Form",font=("SimSun-ExtB",25,"bold"),fg="Red",bg="white")
register_fname_lbl=Label(registerframe,text="First Name :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white")
register_lname_lbl=Label(registerframe,text="Last Name :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white")
register_username_lbl=Label(registerframe,text="Username :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white") 
register_password_lbl=Label(registerframe,text="Password :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white")
register_retypepassword_lbl=Label(registerframe,text="Retype Password :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white")
register_pincode_lbl=Label(registerframe,text="Pincode :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white")
register_address_lbl=Label(registerframe,text="Address :",font=("Calibri",15,"bold"),fg="Darkblue",bg="white")

'All Textfield for register frame'
register_fname_txt=Entry(registerframe,font=("Calibri",15),bg="lightgrey",bd=2)
register_lname_txt=Entry(registerframe,font=("Calibri",15),bg="lightgrey",bd=2)
register_username_txt=Entry(registerframe,font=("Calibri",15),bg="lightgrey",bd=2)
register_password_txt=Entry(registerframe,show="\u2022",font=("Calibri",15),bg="lightgrey",bd=2)
register_retypepassword_txt=Entry(registerframe,show="\u2022",font=("Calibri",15),bg="lightgrey",bd=2)
register_pincode_txt=Entry(registerframe,font=("Calibri",15),bg="lightgrey",bd=2)
register_address_txt=Text(registerframe,height=5,width=37,bg="lightgrey",bd=2,font=("Calibri"))

'All Button for register frame'
register_btn=Button(registerframe,text="Register",font=("Calibri",15),bg="blue",fg="white",cursor="hand2",command=EnterIntoDatabase)
register_cancle_btn=Button(registerframe,text="Cancle",font=("Calibri",15),bg="red",fg="white",cursor="hand2",command=RegisterCancleButtonClick)
loginLink_btn=Button(registerframe,text="Click here to login",font=("Segoe UI Symbol",15,"bold"),fg="Darkblue",bg="white",bd=0,command=LoginLink,cursor="hand2")

'Using place layout manager'
register_title_lbl.place(x=140,y=0)
register_lbl.place(x=22,y=110)
register_fname_lbl.place(x=100,y=160)
register_lname_lbl.place(x=103,y=198)
register_username_lbl.place(x=104,y=237)
register_password_lbl.place(x=107,y=278)
register_retypepassword_lbl.place(x=43,y=318)
register_pincode_lbl.place(x=120,y=355)
register_address_lbl.place(x=120,y=395)

register_fname_txt.place(x=210,y=166,width=300,height=25)
register_lname_txt.place(x=210,y=205,width=300,height=25)
register_username_txt.place(x=210,y=244,width=300,height=25)
register_password_txt.place(x=210,y=283,width=300,height=25)
register_retypepassword_txt.place(x=210,y=322,width=300,height=25)
register_pincode_txt.place(x=210,y=361,width=300,height=25)
register_address_txt.place(x=210,y=400)

register_btn.place(x=320,y=510,height=33,width=74)
register_cancle_btn.place(x=230,y=510,height=33,width=74)
loginLink_btn.place(x=210,y=555,height=35) 

'All Labels for Menu Bar'
register_home_lbl=Label(registerframe,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
register_login_lbl=Label(registerframe,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
register_register_lbl=Label(registerframe,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
register_physiotherapy_lbl=Label(registerframe,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
register_exercise_lbl=Label(registerframe,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
register_home_lbl.place(x=5,y=60)
register_login_lbl.place(x=80,y=60)
register_register_lbl.place(x=155,y=60)
register_physiotherapy_lbl.place(x=253,y=60)
register_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
register_home_lbl.bind("<Button-1>",homeframeEvent)
register_login_lbl.bind("<Button-1>",loginframeEvent)
register_register_lbl.bind("<Button-1>",registerframeEvent)
register_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
register_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

#================PHYSIOTHERAPY FRAME
window.resizable(False,False)
physiotherapyframe=Frame(window,bg="white",width=698,height=600)

physiotherapy_title_lbl=Label(physiotherapyframe,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
physiotherapy_title_lbl.place(x=140,y=0)

'All Labels for Menu Bar'
physiotherapy_home_lbl=Label(physiotherapyframe,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
physiotherapy_login_lbl=Label(physiotherapyframe,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
physiotherapy_register_lbl=Label(physiotherapyframe,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
physiotherapy_physiotherapy_lbl=Label(physiotherapyframe,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
physiotherapy_exercise_lbl=Label(physiotherapyframe,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
physiotherapy_home_lbl.place(x=5,y=60)
physiotherapy_login_lbl.place(x=80,y=60)
physiotherapy_register_lbl.place(x=155,y=60)
physiotherapy_physiotherapy_lbl.place(x=253,y=60)
physiotherapy_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
physiotherapy_home_lbl.bind("<Button-1>",homeframeEvent)
physiotherapy_login_lbl.bind("<Button-1>",loginframeEvent)
physiotherapy_register_lbl.bind("<Button-1>",registerframeEvent)
physiotherapy_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
physiotherapy_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'All Labels for Products of Physiotherapy'
phy_img1=PhotoImage(file=r".\Images\physio product 1.png")
phy_img2=PhotoImage(file=r".\Images\physio product 2.png")
phy_img3=PhotoImage(file=r".\Images\physio product 3.png")
phy_img4=PhotoImage(file=r".\Images\physio product 4.png")
phy_img5=PhotoImage(file=r".\Images\physio product 5.png")
phy_img6=PhotoImage(file=r".\Images\physio product 6.png")

phy_prd1_lbl=Label(physiotherapyframe,bg="red",image=phy_img1,cursor="hand2")
phy_prd2_lbl=Label(physiotherapyframe,bg="blue",image=phy_img2,cursor="hand2")
phy_prd3_lbl=Label(physiotherapyframe,bg="green",image=phy_img3,cursor="hand2")
phy_prd4_lbl=Label(physiotherapyframe,bg="yellow",image=phy_img4,cursor="hand2")
phy_prd5_lbl=Label(physiotherapyframe,bg="orange",image=phy_img5,cursor="hand2")
phy_prd6_lbl=Label(physiotherapyframe,bg="gold",image=phy_img6,cursor="hand2")

phy_prd1_lbl.place(x=45,y=150,height=160,width=170)
phy_prd2_lbl.place(x=260,y=150,height=160,width=170)
phy_prd3_lbl.place(x=480,y=150,height=160,width=170)
phy_prd4_lbl.place(x=45,y=370,height=160,width=170)
phy_prd5_lbl.place(x=260,y=370,height=160,width=170)
phy_prd6_lbl.place(x=480,y=370,height=160,width=170)

'Applying Events on Products'
phy_prd1_lbl.bind("<Button-1>",PhysioPrd1Event)
phy_prd2_lbl.bind("<Button-1>",PhysioPrd2Event)
phy_prd3_lbl.bind("<Button-1>",PhysioPrd3Event)
phy_prd4_lbl.bind("<Button-1>",PhysioPrd4Event)
phy_prd5_lbl.bind("<Button-1>",PhysioPrd5Event)
phy_prd6_lbl.bind("<Button-1>",PhysioPrd6Event)

#================EXERCISE FRAME
window.resizable(False,False)
exerciseframe=Frame(window,bg="white",width=698,height=600)
exercise_title_lbl=Label(exerciseframe,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
exercise_title_lbl.place(x=140,y=0)

'All Labels for Menu Bar'
exercise_home_lbl=Label(exerciseframe,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_login_lbl=Label(exerciseframe,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_register_lbl=Label(exerciseframe,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_physiotherapy_lbl=Label(exerciseframe,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_exercise_lbl=Label(exerciseframe,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
exercise_home_lbl.place(x=5,y=60)
exercise_login_lbl.place(x=80,y=60)
exercise_register_lbl.place(x=155,y=60)
exercise_physiotherapy_lbl.place(x=253,y=60)
exercise_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
exercise_home_lbl.bind("<Button-1>",homeframeEvent)
exercise_login_lbl.bind("<Button-1>",loginframeEvent)
exercise_register_lbl.bind("<Button-1>",registerframeEvent)
exercise_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
exercise_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'All Labels for Products of Exercise'
exer_img1=PhotoImage(file=r".\Images\exercise product 1.png")
exer_img2=PhotoImage(file=r".\Images\exercise product 2.png")
exer_img3=PhotoImage(file=r".\Images\exercise product 3.png")
exer_img4=PhotoImage(file=r".\Images\exercise product 4.png")
exer_img5=PhotoImage(file=r".\Images\exercise product 5.png")
exer_img6=PhotoImage(file=r".\Images\exercise product 6.png")

exercise_prd1_lbl=Label(exerciseframe,bg="red",image=exer_img1,cursor="hand2")
exercise_prd2_lbl=Label(exerciseframe,bg="blue",image=exer_img2,cursor="hand2")
exercise_prd3_lbl=Label(exerciseframe,bg="green",image=exer_img3,cursor="hand2")
exercise_prd4_lbl=Label(exerciseframe,bg="yellow",image=exer_img4,cursor="hand2")
exercise_prd5_lbl=Label(exerciseframe,bg="orange",image=exer_img5,cursor="hand2")
exercise_prd6_lbl=Label(exerciseframe,bg="gold",image=exer_img6,cursor="hand2")

exercise_prd1_lbl.place(x=45,y=150,height=160,width=170)
exercise_prd2_lbl.place(x=260,y=150,height=160,width=170)
exercise_prd3_lbl.place(x=480,y=150,height=160,width=170)
exercise_prd4_lbl.place(x=45,y=370,height=160,width=170)
exercise_prd5_lbl.place(x=260,y=370,height=160,width=170)
exercise_prd6_lbl.place(x=480,y=370,height=160,width=170)

'Applying Events on Products'
exercise_prd1_lbl.bind("<Button-1>",ExercisePrd1Event)
exercise_prd2_lbl.bind("<Button-1>",ExercisePrd2Event)
exercise_prd3_lbl.bind("<Button-1>",ExercisePrd3Event)
exercise_prd4_lbl.bind("<Button-1>",ExercisePrd4Event)
exercise_prd5_lbl.bind("<Button-1>",ExercisePrd5Event)
exercise_prd6_lbl.bind("<Button-1>",ExercisePrd6Event)

#================PHYSIOTHERAPY PRODUCT 1 FRAME
def BuyPhysioProduct1():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd1_detail_qty_txt.get())>=1 and int(phy_prd1_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd1frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Software Diathermy 300 W","Purchased",phy_prd1_detail_qty_txt,32000,result)
          SetEditableFalse()
      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve :
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

def PhysioProduct1_OnLease():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd1_detail_qty_txt.get())>=1 and int(phy_prd1_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd1frame.pack_forget()
        DisplayBillframe.pack()

        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()

        if result:
          DisplayBillDetails("Software Diathermy 300 W","On Leased",phy_prd1_detail_qty_txt,250,result)        
          SetEditableFalse()
      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
    con.rollback()
  finally:
    if con:
     con.close()

window.resizable(False,False) 
PhysioPrd1frame=Frame(window,bg="white",width=600,height=520)

phy_prd1_title_lbl=Label(PhysioPrd1frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
phy_prd1_title_lbl.place(x=80,y=0)

'All Labels for Menu Bar'
phy_prd1_home_lbl=Label(PhysioPrd1frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd1_login_lbl=Label(PhysioPrd1frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd1_register_lbl=Label(PhysioPrd1frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd1_physiotherapy_lbl=Label(PhysioPrd1frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd1_exercise_lbl=Label(PhysioPrd1frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
phy_prd1_home_lbl.place(x=5,y=60)
phy_prd1_login_lbl.place(x=80,y=60)
phy_prd1_register_lbl.place(x=155,y=60)
phy_prd1_physiotherapy_lbl.place(x=253,y=60)
phy_prd1_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
phy_prd1_home_lbl.bind("<Button-1>",homeframeEvent)
phy_prd1_login_lbl.bind("<Button-1>",loginframeEvent)
phy_prd1_register_lbl.bind("<Button-1>",registerframeEvent)
phy_prd1_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
phy_prd1_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
phy_prd_img1=PhotoImage(file=r".\Images\physio product 1 detail.png")
phy_prd1_detail_lbl=Label(PhysioPrd1frame,bg="lightgreen",image=phy_prd_img1)
phy_prd1_detail_qty_lbl=Label(PhysioPrd1frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")

phy_prd1_detail_qty_txt=Entry(PhysioPrd1frame,font=("Calibri",15),bg="lightgrey",bd=2)

phy_prd1_detail_buy_btn=Button(PhysioPrd1frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyPhysioProduct1)
phy_prd1_detail_lease_btn=Button(PhysioPrd1frame,text="Product On Lease",bg="red",fg="white",font=("Calibri",15),cursor="hand2",command=PhysioProduct1_OnLease)

phy_prd1_detail_buyprice_lbl=Label(PhysioPrd1frame,bg="white",text="Buy Product: Rs 32,000.00",font=("Arial Narrow",15,"bold","italic"))
phy_prd1_detail_leaseprice_lbl=Label(PhysioPrd1frame,bg="white",text="Product On Lease: Rs 250.00",font=("Arial Narrow",15,"bold","italic"))

'Using Place Layout Manager'
phy_prd1_detail_lbl.place(x=0,y=120,width=600,height=300)
phy_prd1_detail_qty_lbl.place(x=100,y=460)
phy_prd1_detail_buyprice_lbl.place(x=320,y=388)
phy_prd1_detail_leaseprice_lbl.place(x=276,y=415)
phy_prd1_detail_qty_txt.place(x=220,y=460,width=45,height=35)
phy_prd1_detail_buy_btn.place(x=310,y=460,width=110,height=30)
phy_prd1_detail_lease_btn.place(x=430,y=460,width=153,height=30)

#================PHYSIOTHERAPY PRODUCT 2 FRAME
def BuyPhysioProduct2():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd2_detail_qty_txt.get())>=1 and int(phy_prd2_detail_qty_txt.get())<=20: 
        
        messagebox.showinfo("","Purchase done")
        PhysioPrd2frame.pack_forget()
        DisplayBillframe.pack()

        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()

        if result:
          DisplayBillDetails("Software Diathermy 500 W","Purchased",phy_prd2_detail_qty_txt,44000,result)
          SetEditableFalse() 

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

def PhysioProduct2_OnLease():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd2_detail_qty_txt.get())>=1 and int(phy_prd2_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd2frame.pack_forget()
        DisplayBillframe.pack()

        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Software Diathermy 500 W","On Leased",phy_prd2_detail_qty_txt,300,result)
          SetEditableFalse()
      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")  
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
PhysioPrd2frame=Frame(window,bg="white",width=600,height=520)
phy_prd2_title_lbl=Label(PhysioPrd2frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
phy_prd2_title_lbl.place(x=80,y=0)

phy_prd2_home_lbl=Label(PhysioPrd2frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd2_login_lbl=Label(PhysioPrd2frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd2_register_lbl=Label(PhysioPrd2frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd2_physiotherapy_lbl=Label(PhysioPrd2frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd2_exercise_lbl=Label(PhysioPrd2frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
phy_prd2_home_lbl.place(x=5,y=60)
phy_prd2_login_lbl.place(x=80,y=60)
phy_prd2_register_lbl.place(x=155,y=60)
phy_prd2_physiotherapy_lbl.place(x=253,y=60)
phy_prd2_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
phy_prd2_home_lbl.bind("<Button-1>",homeframeEvent)
phy_prd2_login_lbl.bind("<Button-1>",loginframeEvent)
phy_prd2_register_lbl.bind("<Button-1>",registerframeEvent)
phy_prd2_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
phy_prd2_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
phy_prd_img2=PhotoImage(file=r".\Images\physio product 2 detail.png")
phy_prd2_detail_lbl=Label(PhysioPrd2frame,bg="lightgreen",image=phy_prd_img2)
phy_prd2_detail_qty_lbl=Label(PhysioPrd2frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")

phy_prd2_detail_qty_txt=Entry(PhysioPrd2frame,font=("Calibri",15),bg="lightgrey",bd=2)

phy_prd2_detail_buy_btn=Button(PhysioPrd2frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyPhysioProduct2)
phy_prd2_detail_lease_btn=Button(PhysioPrd2frame,text="Product On Lease",bg="red",fg="white",font=("Calibri",15),cursor="hand2",command=PhysioProduct2_OnLease)

phy_prd2_detail_buyprice_lbl=Label(PhysioPrd2frame,bg="white",text="Buy Product: Rs 44,000.00",font=("Arial Narrow",15,"bold","italic"))
phy_prd2_detail_leaseprice_lbl=Label(PhysioPrd2frame,bg="white",text="Product On Lease: Rs 300.00",font=("Arial Narrow",15,"bold","italic"))

'Using Place Layout Manager'
phy_prd2_detail_lbl.place(x=0,y=120,width=600,height=300)
phy_prd2_detail_qty_lbl.place(x=100,y=467)
phy_prd2_detail_buyprice_lbl.place(x=315,y=405)
phy_prd2_detail_leaseprice_lbl.place(x=276,y=430)
phy_prd2_detail_qty_txt.place(x=220,y=471,width=45,height=35)
phy_prd2_detail_buy_btn.place(x=310,y=470,width=110,height=30)
phy_prd2_detail_lease_btn.place(x=430,y=470,width=153,height=30)

#================PHYSIOTHERAPY PRODUCT 3 FRAME
def BuyPhysioProduct3():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd3_detail_qty_txt.get())>=1 and int(phy_prd3_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd3frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Cervical Cum Lumbar Traction","Purchased",phy_prd3_detail_qty_txt,25000,result)       
          SetEditableFalse()
      
      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

def PhysioProduct3_OnLease():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd3_detail_qty_txt.get())>=1 and int(phy_prd3_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd3frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Cervical Cum Lumbar Traction","On Leased",phy_prd3_detail_qty_txt,300,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
PhysioPrd3frame=Frame(window,bg="white",width=600,height=520)
phy_prd3_title_lbl=Label(PhysioPrd3frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
phy_prd3_title_lbl.place(x=80,y=0)

phy_prd3_home_lbl=Label(PhysioPrd3frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd3_login_lbl=Label(PhysioPrd3frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd3_register_lbl=Label(PhysioPrd3frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd3_physiotherapy_lbl=Label(PhysioPrd3frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd3_exercise_lbl=Label(PhysioPrd3frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
phy_prd3_home_lbl.place(x=5,y=60)
phy_prd3_login_lbl.place(x=80,y=60)
phy_prd3_register_lbl.place(x=155,y=60)
phy_prd3_physiotherapy_lbl.place(x=253,y=60)
phy_prd3_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
phy_prd3_home_lbl.bind("<Button-1>",homeframeEvent)
phy_prd3_login_lbl.bind("<Button-1>",loginframeEvent)
phy_prd3_register_lbl.bind("<Button-1>",registerframeEvent)
phy_prd3_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
phy_prd3_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
phy_prd_img3=PhotoImage(file=r".\Images\physio product 3 detail.png")
phy_prd3_detail_lbl=Label(PhysioPrd3frame,bg="lightgreen",image=phy_prd_img3)
phy_prd3_detail_qty_lbl=Label(PhysioPrd3frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
phy_prd3_detail_qty_txt=Entry(PhysioPrd3frame,font=("Calibri",15),bg="lightgrey",bd=2)
phy_prd3_detail_buy_btn=Button(PhysioPrd3frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyPhysioProduct3)
phy_prd3_detail_lease_btn=Button(PhysioPrd3frame,text="Product On Lease",bg="red",fg="white",font=("Calibri",15),cursor="hand2",command=PhysioProduct3_OnLease)
phy_prd3_detail_buyprice_lbl=Label(PhysioPrd3frame,bg="white",text="Buy Product: Rs 25,000.00",font=("Arial Narrow",15,"bold","italic"))
phy_prd3_detail_leaseprice_lbl=Label(PhysioPrd3frame,bg="white",text="Product On Lease: Rs 300.00",font=("Arial Narrow",15,"bold","italic"))

'Using Place Layout Manager'
phy_prd3_detail_lbl.place(x=0,y=120,width=600,height=300)
phy_prd3_detail_qty_lbl.place(x=100,y=467)
phy_prd3_detail_buyprice_lbl.place(x=315,y=390)
phy_prd3_detail_leaseprice_lbl.place(x=276,y=420)
phy_prd3_detail_qty_txt.place(x=220,y=471,width=45,height=35)
phy_prd3_detail_buy_btn.place(x=310,y=470,width=110,height=30)
phy_prd3_detail_lease_btn.place(x=430,y=470,width=153,height=30)

#================PHYSIOTHERAPY PRODUCT 4 FRAME
def BuyPhysioProduct4():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd4_detail_qty_txt.get())>=1 and int(phy_prd4_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd4frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Computerized IFT","Purchased",phy_prd4_detail_qty_txt,25000,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close() 
 
def PhysioProduct4_OnLease():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd4_detail_qty_txt.get())>=1 and int(phy_prd4_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd4frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()

        if result:
          DisplayBillDetails("Computerized IFT","On Leased",phy_prd4_detail_qty_txt,150,result)
          SetEditableFalse()
      
      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer") 
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
PhysioPrd4frame=Frame(window,bg="white",width=600,height=530)
phy_prd4_title_lbl=Label(PhysioPrd4frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
phy_prd4_title_lbl.place(x=80,y=0)

phy_prd4_home_lbl=Label(PhysioPrd4frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd4_login_lbl=Label(PhysioPrd4frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd4_register_lbl=Label(PhysioPrd4frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd4_physiotherapy_lbl=Label(PhysioPrd4frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd4_exercise_lbl=Label(PhysioPrd4frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
phy_prd4_home_lbl.place(x=5,y=60)
phy_prd4_login_lbl.place(x=80,y=60)
phy_prd4_register_lbl.place(x=155,y=60)
phy_prd4_physiotherapy_lbl.place(x=253,y=60)
phy_prd4_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
phy_prd4_home_lbl.bind("<Button-1>",homeframeEvent)
phy_prd4_login_lbl.bind("<Button-1>",loginframeEvent)
phy_prd4_register_lbl.bind("<Button-1>",registerframeEvent)
phy_prd4_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
phy_prd4_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
phy_prd_img4=PhotoImage(file=r".\Images\physio product 4 detail.png")
phy_prd4_detail_lbl=Label(PhysioPrd4frame,bg="lightgreen",image=phy_prd_img4)
phy_prd4_detail_qty_lbl=Label(PhysioPrd4frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
phy_prd4_detail_qty_txt=Entry(PhysioPrd4frame,font=("Calibri",15),bg="lightgrey",bd=2)
phy_prd4_detail_buy_btn=Button(PhysioPrd4frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyPhysioProduct4)
phy_prd4_detail_lease_btn=Button(PhysioPrd4frame,text="Product On Lease",bg="red",fg="white",font=("Calibri",15),cursor="hand2",command=PhysioProduct4_OnLease)
phy_prd4_detail_buyprice_lbl=Label(PhysioPrd4frame,bg="white",text="Buy Product: Rs 25,000.00",font=("Arial Narrow",15,"bold","italic"))
phy_prd4_detail_leaseprice_lbl=Label(PhysioPrd4frame,bg="white",text="Product On Lease: Rs 150.00",font=("Arial Narrow",15,"bold","italic"))

'Using Place Layout Manager'
phy_prd4_detail_lbl.place(x=0,y=120,width=600,height=300)
phy_prd4_detail_qty_lbl.place(x=100,y=485)
phy_prd4_detail_buyprice_lbl.place(x=315,y=420)
phy_prd4_detail_leaseprice_lbl.place(x=270,y=447)
phy_prd4_detail_qty_txt.place(x=220,y=485,width=45,height=35)
phy_prd4_detail_buy_btn.place(x=310,y=485,width=110,height=30)
phy_prd4_detail_lease_btn.place(x=430,y=485,width=153,height=30)

#================PHYSIOTHERAPY PRODUCT 5 FRAME
def BuyPhysioProduct5():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd5_detail_qty_txt.get())>=1 and int(phy_prd5_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd5frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("4 Channel Tense","Purchased",phy_prd5_detail_qty_txt,8000,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

def PhysioProduct5_OnLease():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd5_detail_qty_txt.get())>=1 and int(phy_prd5_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd5frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("4 Channel Tense","On Leased",phy_prd5_detail_qty_txt,150,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")  
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()   

window.resizable(False,False) 
PhysioPrd5frame=Frame(window,bg="white",width=600,height=530)
phy_prd5_title_lbl=Label(PhysioPrd5frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
phy_prd5_title_lbl.place(x=80,y=0)

phy_prd5_home_lbl=Label(PhysioPrd5frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd5_login_lbl=Label(PhysioPrd5frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd5_register_lbl=Label(PhysioPrd5frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd5_physiotherapy_lbl=Label(PhysioPrd5frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd5_exercise_lbl=Label(PhysioPrd5frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
phy_prd5_home_lbl.place(x=5,y=60)
phy_prd5_login_lbl.place(x=80,y=60)
phy_prd5_register_lbl.place(x=155,y=60)
phy_prd5_physiotherapy_lbl.place(x=253,y=60)
phy_prd5_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
phy_prd5_home_lbl.bind("<Button-1>",homeframeEvent)
phy_prd5_login_lbl.bind("<Button-1>",loginframeEvent)
phy_prd5_register_lbl.bind("<Button-1>",registerframeEvent)
phy_prd5_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
phy_prd5_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
phy_prd_img5=PhotoImage(file=r".\Images\physio product 5 detail.png")
phy_prd5_detail_lbl=Label(PhysioPrd5frame,bg="lightgreen",image=phy_prd_img5)
phy_prd5_detail_qty_lbl=Label(PhysioPrd5frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
phy_prd5_detail_qty_txt=Entry(PhysioPrd5frame,font=("Calibri",15),bg="lightgrey",bd=2)
phy_prd5_detail_buy_btn=Button(PhysioPrd5frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyPhysioProduct5)
phy_prd5_detail_lease_btn=Button(PhysioPrd5frame,text="Product On Lease",bg="red",fg="white",font=("Calibri",15),cursor="hand2",command=PhysioProduct5_OnLease)
phy_prd5_detail_buyprice_lbl=Label(PhysioPrd5frame,bg="white",text="Buy Product: Rs 8,000.00",font=("Arial Narrow",15,"bold","italic"))
phy_prd5_detail_leaseprice_lbl=Label(PhysioPrd5frame,bg="white",text="Product On Lease: Rs 150.00",font=("Arial Narrow",15,"bold","italic"))

'Using Place Layout Manager'
phy_prd5_detail_lbl.place(x=0,y=120,width=600,height=300)
phy_prd5_detail_qty_lbl.place(x=100,y=485)
phy_prd5_detail_buyprice_lbl.place(x=315,y=420)
phy_prd5_detail_leaseprice_lbl.place(x=270,y=447)
phy_prd5_detail_qty_txt.place(x=220,y=485,width=45,height=35)
phy_prd5_detail_buy_btn.place(x=310,y=485,width=110,height=30)
phy_prd5_detail_lease_btn.place(x=430,y=485,width=153,height=30)

#================PHYSIOTHERAPY PRODUCT 6 FRAME
def BuyPhysioProduct6():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd6_detail_qty_txt.get())>=1 and int(phy_prd6_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd6frame.pack_forget()
        DisplayBillframe.pack()

        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("CPM","Purchased",phy_prd6_detail_qty_txt,25000,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

def PhysioProduct6_OnLease():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(phy_prd6_detail_qty_txt.get())>=1 and int(phy_prd6_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        PhysioPrd6frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:  
          DisplayBillDetails("CPM","On Leased",phy_prd6_detail_qty_txt,300,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")    
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
PhysioPrd6frame=Frame(window,bg="white",width=600,height=530)
phy_prd6_title_lbl=Label(PhysioPrd6frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
phy_prd6_title_lbl.place(x=80,y=0)

phy_prd6_home_lbl=Label(PhysioPrd6frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd6_login_lbl=Label(PhysioPrd6frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd6_register_lbl=Label(PhysioPrd6frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd6_physiotherapy_lbl=Label(PhysioPrd6frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
phy_prd6_exercise_lbl=Label(PhysioPrd6frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
phy_prd6_home_lbl.place(x=5,y=60)
phy_prd6_login_lbl.place(x=80,y=60)
phy_prd6_register_lbl.place(x=155,y=60)
phy_prd6_physiotherapy_lbl.place(x=253,y=60)
phy_prd6_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
phy_prd6_home_lbl.bind("<Button-1>",homeframeEvent)
phy_prd6_login_lbl.bind("<Button-1>",loginframeEvent)
phy_prd6_register_lbl.bind("<Button-1>",registerframeEvent)
phy_prd6_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
phy_prd6_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
phy_prd_img6=PhotoImage(file=r".\Images\physio product 6 detail.png")
phy_prd6_detail_lbl=Label(PhysioPrd6frame,bg="lightgreen",image=phy_prd_img6)
phy_prd6_detail_qty_lbl=Label(PhysioPrd6frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
phy_prd6_detail_qty_txt=Entry(PhysioPrd6frame,font=("Calibri",15),bg="lightgrey",bd=2)
phy_prd6_detail_buy_btn=Button(PhysioPrd6frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyPhysioProduct6)
phy_prd6_detail_lease_btn=Button(PhysioPrd6frame,text="Product On Lease",bg="red",fg="white",font=("Calibri",15),cursor="hand2",command=PhysioProduct6_OnLease)
phy_prd6_detail_buyprice_lbl=Label(PhysioPrd6frame,bg="white",text="Buy Product: Rs 25,000.00",font=("Arial Narrow",15,"bold","italic"))
phy_prd6_detail_leaseprice_lbl=Label(PhysioPrd6frame,bg="white",text="Product On Lease: Rs 300.00",font=("Arial Narrow",15,"bold","italic"))

'Using Place Layout Manager'
phy_prd6_detail_lbl.place(x=0,y=120,width=600,height=300)
phy_prd6_detail_qty_lbl.place(x=100,y=485)
phy_prd6_detail_buyprice_lbl.place(x=315,y=420)
phy_prd6_detail_leaseprice_lbl.place(x=270,y=447)
phy_prd6_detail_qty_txt.place(x=220,y=485,width=45,height=35)
phy_prd6_detail_buy_btn.place(x=310,y=485,width=110,height=30)
phy_prd6_detail_lease_btn.place(x=430,y=485,width=153,height=30)

#================EXERCISE PRODUCT 1 FRAME
def BuyExerciseProduct1():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(exer_prd1_detail_qty_txt.get())>=1 and int(exer_prd1_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        ExercisePrd1frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Ankle Excerciser","Purchased",exer_prd1_detail_qty_txt,3000,result)
          SetEditableFalse() 

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    else:
     messagebox.showerror("","Please Login and Try")
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
 
window.resizable(False,False) 
ExercisePrd1frame=Frame(window,bg="white",width=600,height=500)
exercise_prd1_title_lbl=Label(ExercisePrd1frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
exercise_prd1_title_lbl.place(x=80,y=0)

exercise_prd1_home_lbl=Label(ExercisePrd1frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd1_login_lbl=Label(ExercisePrd1frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd1_register_lbl=Label(ExercisePrd1frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd1_physiotherapy_lbl=Label(ExercisePrd1frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd1_exercise_lbl=Label(ExercisePrd1frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
exercise_prd1_home_lbl.place(x=5,y=60)
exercise_prd1_login_lbl.place(x=80,y=60)
exercise_prd1_register_lbl.place(x=155,y=60)
exercise_prd1_physiotherapy_lbl.place(x=253,y=60)
exercise_prd1_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
exercise_prd1_home_lbl.bind("<Button-1>",homeframeEvent)
exercise_prd1_login_lbl.bind("<Button-1>",loginframeEvent)
exercise_prd1_register_lbl.bind("<Button-1>",registerframeEvent)
exercise_prd1_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
exercise_prd1_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
exer_prd_img1=PhotoImage(file=r".\Images\exercise product 1 detail.png")
exer_prd1_detail_lbl=Label(ExercisePrd1frame,bg="lightgreen",image=exer_prd_img1)
exer_prd1_detail_qty_lbl=Label(ExercisePrd1frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
exer_prd1_detail_qty_txt=Entry(ExercisePrd1frame,font=("Calibri",15),bg="lightgrey",bd=2)
exer_prd1_detail_buy_btn=Button(ExercisePrd1frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyExerciseProduct1)
exer_prd1_detail_buyprice_lbl=Label(ExercisePrd1frame,bg="white",text="Buy Product: Rs 3,000.00",font=("Arial Narrow",20,"bold","italic"))

'Using Place Layout Manager'
exer_prd1_detail_lbl.place(x=0,y=120,width=600,height=300)
exer_prd1_detail_qty_lbl.place(x=200,y=427)
exer_prd1_detail_buyprice_lbl.place(x=255,y=360)
exer_prd1_detail_qty_txt.place(x=320,y=431,width=45,height=35)
exer_prd1_detail_buy_btn.place(x=410,y=430,width=110,height=30)

#================EXERCISE PRODUCT 2 FRAME
def BuyExerciseProduct2():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(exer_prd2_detail_qty_txt.get())>=1 and int(exer_prd2_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        ExercisePrd2frame.pack_forget()
        DisplayBillframe.pack()
        
        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Finger Weight","Purchased",exer_prd2_detail_qty_txt,3200,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
ExercisePrd2frame=Frame(window,bg="white",width=600,height=510)
exercise_prd2_title_lbl=Label(ExercisePrd2frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
exercise_prd2_title_lbl.place(x=80,y=0)

exercise_prd2_home_lbl=Label(ExercisePrd2frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd2_login_lbl=Label(ExercisePrd2frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd2_register_lbl=Label(ExercisePrd2frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd2_physiotherapy_lbl=Label(ExercisePrd2frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd2_exercise_lbl=Label(ExercisePrd2frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
exercise_prd2_home_lbl.place(x=5,y=60)
exercise_prd2_login_lbl.place(x=80,y=60)
exercise_prd2_register_lbl.place(x=155,y=60)
exercise_prd2_physiotherapy_lbl.place(x=253,y=60)
exercise_prd2_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
exercise_prd2_home_lbl.bind("<Button-1>",homeframeEvent)
exercise_prd2_login_lbl.bind("<Button-1>",loginframeEvent)
exercise_prd2_register_lbl.bind("<Button-1>",registerframeEvent)
exercise_prd2_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
exercise_prd2_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
exer_prd_img2=PhotoImage(file=r".\Images\exercise product 2 detail.png")
exer_prd2_detail_lbl=Label(ExercisePrd2frame,bg="lightgreen",image=exer_prd_img2)
exer_prd2_detail_qty_lbl=Label(ExercisePrd2frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
exer_prd2_detail_qty_txt=Entry(ExercisePrd2frame,font=("Calibri",15),bg="lightgrey",bd=2)
exer_prd2_detail_buy_btn=Button(ExercisePrd2frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyExerciseProduct2)
exer_prd2_detail_buyprice_lbl=Label(ExercisePrd2frame,bg="white",text="Buy Product: Rs 3,200.00",font=("Arial Narrow",20,"bold","italic"))

'Using Place Layout Manager'
exer_prd2_detail_lbl.place(x=0,y=120,width=600,height=300)
exer_prd2_detail_qty_lbl.place(x=200,y=460)
exer_prd2_detail_buyprice_lbl.place(x=235,y=420)
exer_prd2_detail_qty_txt.place(x=320,y=460,width=45,height=35)
exer_prd2_detail_buy_btn.place(x=410,y=460,width=110,height=30)

#================EXERCISE PRODUCT 3 FRAME
def BuyExerciseProduct3():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(exer_prd3_detail_qty_txt.get())>=1 and int(exer_prd3_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        ExercisePrd3frame.pack_forget()
        DisplayBillframe.pack()

        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Gripper","Purchased",exer_prd3_detail_qty_txt,500,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
ExercisePrd3frame=Frame(window,bg="white",width=600,height=510)
exercise_prd3_title_lbl=Label(ExercisePrd3frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
exercise_prd3_title_lbl.place(x=80,y=0)

exercise_prd3_home_lbl=Label(ExercisePrd3frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd3_login_lbl=Label(ExercisePrd3frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd3_register_lbl=Label(ExercisePrd3frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd3_physiotherapy_lbl=Label(ExercisePrd3frame,text="Physiotherapy",font=("Tahoma",15,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd3_exercise_lbl=Label(ExercisePrd3frame,text="Excercise",font=("Tahoma",15,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
exercise_prd3_home_lbl.place(x=5,y=60)
exercise_prd3_login_lbl.place(x=80,y=60)
exercise_prd3_register_lbl.place(x=155,y=60)
exercise_prd3_physiotherapy_lbl.place(x=253,y=60)
exercise_prd3_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
exercise_prd3_home_lbl.bind("<Button-1>",homeframeEvent)
exercise_prd3_login_lbl.bind("<Button-1>",loginframeEvent)
exercise_prd3_register_lbl.bind("<Button-1>",registerframeEvent)
exercise_prd3_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
exercise_prd3_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
exer_prd_img3=PhotoImage(file=r".\Images\exercise product 3 detail.png")
exer_prd3_detail_lbl=Label(ExercisePrd3frame,bg="lightgreen",image=exer_prd_img3)
exer_prd3_detail_qty_lbl=Label(ExercisePrd3frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
exer_prd3_detail_qty_txt=Entry(ExercisePrd3frame,font=("Calibri",15),bg="lightgrey",bd=2)
exer_prd3_detail_buy_btn=Button(ExercisePrd3frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyExerciseProduct3)
exer_prd3_detail_buyprice_lbl=Label(ExercisePrd3frame,bg="white",text="Buy Product: Rs 500.00",font=("Arial Narrow",20,"bold","italic"))

'Using Place Layout Manager'
exer_prd3_detail_lbl.place(x=0,y=120,width=600,height=300)
exer_prd3_detail_qty_lbl.place(x=200,y=460)
exer_prd3_detail_buyprice_lbl.place(x=235,y=420)
exer_prd3_detail_qty_txt.place(x=320,y=460,width=45,height=35)
exer_prd3_detail_buy_btn.place(x=410,y=460,width=110,height=30)

#================EXERCISE PRODUCT 4 FRAME
def BuyExerciseProduct4():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(exer_prd4_detail_qty_txt.get())>=1 and int(exer_prd4_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        ExercisePrd4frame.pack_forget()
        DisplayBillframe.pack()

        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          DisplayBillDetails("Adjustable Shoulder Wheel","Purchased",exer_prd4_detail_qty_txt,3000,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
ExercisePrd4frame=Frame(window,bg="white",width=600,height=510)
exercise_prd4_title_lbl=Label(ExercisePrd4frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
exercise_prd4_title_lbl.place(x=80,y=0)

exercise_prd4_home_lbl=Label(ExercisePrd4frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd4_login_lbl=Label(ExercisePrd4frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd4_register_lbl=Label(ExercisePrd4frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd4_physiotherapy_lbl=Label(ExercisePrd4frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd4_exercise_lbl=Label(ExercisePrd4frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
exercise_prd4_home_lbl.place(x=5,y=60)
exercise_prd4_login_lbl.place(x=80,y=60)
exercise_prd4_register_lbl.place(x=155,y=60)
exercise_prd4_physiotherapy_lbl.place(x=253,y=60)
exercise_prd4_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
exercise_prd4_home_lbl.bind("<Button-1>",homeframeEvent)
exercise_prd4_login_lbl.bind("<Button-1>",loginframeEvent)
exercise_prd4_register_lbl.bind("<Button-1>",registerframeEvent)
exercise_prd4_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
exercise_prd4_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
exer_prd_img4=PhotoImage(file=r".\Images\exercise product 4 detail.png")
exer_prd4_detail_lbl=Label(ExercisePrd4frame,bg="lightgreen",image=exer_prd_img4)
exer_prd4_detail_qty_lbl=Label(ExercisePrd4frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
exer_prd4_detail_qty_txt=Entry(ExercisePrd4frame,font=("Calibri",15),bg="lightgrey",bd=2)
exer_prd4_detail_buy_btn=Button(ExercisePrd4frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyExerciseProduct4)
exer_prd4_detail_buyprice_lbl=Label(ExercisePrd4frame,bg="white",text="Buy Product: Rs 3,000.00",font=("Arial Narrow",20,"bold","italic"))

'Using Place Layout Manager'
exer_prd4_detail_lbl.place(x=0,y=120,width=600,height=300)
exer_prd4_detail_qty_lbl.place(x=200,y=460)
exer_prd4_detail_buyprice_lbl.place(x=235,y=420)
exer_prd4_detail_qty_txt.place(x=320,y=460,width=45,height=35)
exer_prd4_detail_buy_btn.place(x=410,y=460,width=110,height=30)

#================EXERCISE PRODUCT 5 FRAME
def BuyExerciseProduct5():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(exer_prd5_detail_qty_txt.get())>=1 and int(exer_prd5_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        ExercisePrd5frame.pack_forget()
        DisplayBillframe.pack()

        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        
        if result:
          DisplayBillDetails("Static Cycle","Purchased",exer_prd5_detail_qty_txt,11000,result)
          SetEditableFalse()

      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
ExercisePrd5frame=Frame(window,bg="white",width=600,height=510)
exercise_prd5_title_lbl=Label(ExercisePrd5frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
exercise_prd5_title_lbl.place(x=80,y=0)

exercise_prd5_home_lbl=Label(ExercisePrd5frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd5_login_lbl=Label(ExercisePrd5frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd5_register_lbl=Label(ExercisePrd5frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd5_physiotherapy_lbl=Label(ExercisePrd5frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd5_exercise_lbl=Label(ExercisePrd5frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
exercise_prd5_home_lbl.place(x=5,y=60)
exercise_prd5_login_lbl.place(x=80,y=60)
exercise_prd5_register_lbl.place(x=155,y=60)
exercise_prd5_physiotherapy_lbl.place(x=253,y=60)
exercise_prd5_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
exercise_prd5_home_lbl.bind("<Button-1>",homeframeEvent)
exercise_prd5_login_lbl.bind("<Button-1>",loginframeEvent)
exercise_prd5_register_lbl.bind("<Button-1>",registerframeEvent)
exercise_prd5_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
exercise_prd5_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
exer_prd_img5=PhotoImage(file=r".\Images\exercise product 5 detail.png")
exer_prd5_detail_lbl=Label(ExercisePrd5frame,bg="lightgreen",image=exer_prd_img5)
exer_prd5_detail_qty_lbl=Label(ExercisePrd5frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
exer_prd5_detail_qty_txt=Entry(ExercisePrd5frame,font=("Calibri",15),bg="lightgrey",bd=2)
exer_prd5_detail_buy_btn=Button(ExercisePrd5frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyExerciseProduct5)
exer_prd5_detail_buyprice_lbl=Label(ExercisePrd5frame,bg="white",text="Buy Product: Rs 11,000.00",font=("Arial Narrow",20,"bold","italic"))

'Using Place Layout Manager'
exer_prd5_detail_lbl.place(x=0,y=120,width=600,height=300)
exer_prd5_detail_qty_lbl.place(x=200,y=460)
exer_prd5_detail_buyprice_lbl.place(x=235,y=418)
exer_prd5_detail_qty_txt.place(x=320,y=460,width=45,height=35)
exer_prd5_detail_buy_btn.place(x=410,y=460,width=110,height=30)

#================EXERCISE PRODUCT 6 FRAME
def BuyExerciseProduct6():
  con= mysql.connector.connect(host="localhost",user="root",password="",database="physio-equip surgical")
  try:
    if LoginStatus.loginStatus==1:
      
      if int(exer_prd6_detail_qty_txt.get())>=1 and int(exer_prd6_detail_qty_txt.get())<=20: 
        messagebox.showinfo("","Purchase done")
        ExercisePrd6frame.pack_forget()
        DisplayBillframe.pack()

        cur=con.cursor()
        sql="select * from user where username='{}';".format(LoginStatus.loginUsername)
        cur.execute(sql)
        result=cur.fetchall()
        if result:
          sql="insert into "
          DisplayBillDetails("Hydrocollator","Purchased",exer_prd6_detail_qty_txt,5000,result)
          SetEditableFalse()
      
      else:
        messagebox.showerror("","Enter Quantity Greater Than EqualTo 1\n      OR\nEnter Quantity Less Than EqualTo 20")  
    
    else:
     messagebox.showerror("","Please Login and Try")
  
  except ValueError as ve:
     messagebox.showerror("Invalid Quantity","Enter Valid Quantity\n    OR\nYou Have Entered Invalid Integer")
  except Exception as e:
    messagebox.showerror("XAMPP ERROR","ODBC CONNECTION FAIL")
  finally:
    if con:
     con.close()

window.resizable(False,False) 
ExercisePrd6frame=Frame(window,bg="white",width=600,height=510)
exercise_prd6_title_lbl=Label(ExercisePrd6frame,text="Physio-Equip Surgical",font=("Times new Roman",35,"bold","italic"),fg="purple",bg="white")
exercise_prd6_title_lbl.place(x=80,y=0)

exercise_prd6_home_lbl=Label(ExercisePrd6frame,text="Home",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd6_login_lbl=Label(ExercisePrd6frame,text="Login",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd6_register_lbl=Label(ExercisePrd6frame,text="Register",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd6_physiotherapy_lbl=Label(ExercisePrd6frame,text="Physiotherapy",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")
exercise_prd6_exercise_lbl=Label(ExercisePrd6frame,text="Excercise",font=("Tahoma",14,"bold"),fg="hot pink",bg="white",cursor="hand2")

'Using Place Layout Manager'
exercise_prd6_home_lbl.place(x=5,y=60)
exercise_prd6_login_lbl.place(x=80,y=60)
exercise_prd6_register_lbl.place(x=155,y=60)
exercise_prd6_physiotherapy_lbl.place(x=253,y=60)
exercise_prd6_exercise_lbl.place(x=410,y=60)

'Applying Events on Labels'
exercise_prd6_home_lbl.bind("<Button-1>",homeframeEvent)
exercise_prd6_login_lbl.bind("<Button-1>",loginframeEvent)
exercise_prd6_register_lbl.bind("<Button-1>",registerframeEvent)
exercise_prd6_physiotherapy_lbl.bind("<Button-1>",physiotherapyframeEvent)
exercise_prd6_exercise_lbl.bind("<Button-1>",exerciseframeEvent)

'Widgets for Displaying Details'
exer_prd_img6=PhotoImage(file=r".\Images\exercise product 6 detail.png")
exer_prd6_detail_lbl=Label(ExercisePrd6frame,bg="lightgreen",image=exer_prd_img6)
exer_prd6_detail_qty_lbl=Label(ExercisePrd6frame,text="Quantity :",font=("Calibri",19,"bold"),bg="white")
exer_prd6_detail_qty_txt=Entry(ExercisePrd6frame,font=("Calibri",15),bg="lightgrey",bd=2)
exer_prd6_detail_buy_btn=Button(ExercisePrd6frame,text="Buy Product",bg="blue",fg="white",font=("Calibri",15),cursor="hand2",command=BuyExerciseProduct6)
exer_prd6_detail_buyprice_lbl=Label(ExercisePrd6frame,bg="white",text="Buy Product: Rs 5,000.00",font=("Arial Narrow",20,"bold","italic"))

'Using Place Layout Manager'
exer_prd6_detail_lbl.place(x=0,y=120,width=600,height=300)
exer_prd6_detail_qty_lbl.place(x=200,y=460)
exer_prd6_detail_buyprice_lbl.place(x=235,y=418)
exer_prd6_detail_qty_txt.place(x=320,y=460,width=45,height=35)
exer_prd6_detail_buy_btn.place(x=410,y=460,width=110,height=30)

#==================DISPLAY BILL
window.resizable(False,False)
DisplayBillframe=Frame(window,bg="white",width=750,height=650)

DisplayBill_title_lbl=Label(DisplayBillframe,text="Physio-Equip Surgical",font=("Times new Roman",40,"bold","italic"),fg="purple",bg="white")
DisplayBill_title_lbl.place(x=100,y=0)

DisplayBill_heading_lbl=Label(DisplayBillframe,text="YOUR BILL",font=("Tahoma",30,"bold"),fg="blue2",bg="white")
DisplayBill_UserDetails_lbl=Label(DisplayBillframe,text="User Details",font=("Tahoma",20,"bold"),fg="firebrick1",bg="white")
DisplayBill_DeliveryDetails_lbl=Label(DisplayBillframe,text="Delivery Details",font=("Tahoma",20,"bold"),fg="firebrick1",bg="white")
DisplayBill_ProductDetails_lbl=Label(DisplayBillframe,text="Product Details",font=("Tahoma",20,"bold"),fg="firebrick1",bg="white")
DisplayBill_PricingDetails_lbl=Label(DisplayBillframe,text="Pricing",font=("Tahoma",20,"bold"),fg="firebrick1",bg="white")

DisplayBill_heading_lbl.place(x=220,y=80)
DisplayBill_UserDetails_lbl.place(x=30,y=150)
DisplayBill_DeliveryDetails_lbl.place(x=400,y=150)
DisplayBill_ProductDetails_lbl.place(x=30,y=450)
DisplayBill_PricingDetails_lbl.place(x=400,y=450)

DisplayBill_User_fname_lbl=Label(DisplayBillframe,text="First Name :",font=("Tahoma",15),bg="white")
DisplayBill_User_lname_lbl=Label(DisplayBillframe,text="Last Name :",font=("Tahoma",15),bg="white")
DisplayBill_User_uname_lbl=Label(DisplayBillframe,text="User Name :",font=("Tahoma",15),bg="white")
DisplayBill_User_pincode_lbl=Label(DisplayBillframe,text="Pincode :",font=("Tahoma",15),bg="white")
DisplayBill_User_address_lbl=Label(DisplayBillframe,text="Address :",font=("Tahoma",15),bg="white")

DisplayBill_User_fname_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_User_lname_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_User_uname_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_User_pincode_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_User_address_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_User_address_txt=Entry(DisplayBillframe,bg="lightgrey",bd=2,font=("Calibri"))

DisplayBill_User_fname_lbl.place(x=30,y=200)
DisplayBill_User_lname_lbl.place(x=30,y=235)
DisplayBill_User_uname_lbl.place(x=25,y=265)
DisplayBill_User_pincode_lbl.place(x=55,y=295)
DisplayBill_User_address_lbl.place(x=55,y=335)

DisplayBill_User_fname_txt.place(x=155,y=205,width=180,height=25)
DisplayBill_User_lname_txt.place(x=155,y=238,width=180,height=25)
DisplayBill_User_uname_txt.place(x=155,y=271,width=180,height=25)
DisplayBill_User_pincode_txt.place(x=155,y=304,width=180,height=25)
DisplayBill_User_address_txt.place(x=155,y=337,height=60,width=180)

DisplayBill_Delivery_fname_lbl=Label(DisplayBillframe,text="First Name :",font=("Tahoma",15),bg="white")
DisplayBill_Delivery_lname_lbl=Label(DisplayBillframe,text="Last Name :",font=("Tahoma",15),bg="white")
DisplayBill_Delivery_prdname_lbl=Label(DisplayBillframe,text="Product Name :",font=("Tahoma",15),bg="white")
DisplayBill_Delivery_deliverydate_lbl=Label(DisplayBillframe,text="Delivered By :",font=("Tahoma",15),bg="white")
DisplayBill_Delivery_pincode_lbl=Label(DisplayBillframe,text="Pincode :",font=("Tahoma",15),bg="white")
DisplayBill_Delivery_address_lbl=Label(DisplayBillframe,text="Address :",font=("Tahoma",15),bg="white")

DisplayBill_Delivery_fname_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_Delivery_lname_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_Delivery_prdname_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_Delivery_deliverydate_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_Delivery_pincode_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_Delivery_address_txt=Entry(DisplayBillframe,bg="lightgrey",bd=2,font=("Calibri"))

DisplayBill_Delivery_fname_lbl.place(x=400,y=195)
DisplayBill_Delivery_lname_lbl.place(x=400,y=230)
DisplayBill_Delivery_prdname_lbl.place(x=370,y=265)
DisplayBill_Delivery_deliverydate_lbl.place(x=383,y=300)
DisplayBill_Delivery_pincode_lbl.place(x=427,y=330)
DisplayBill_Delivery_address_lbl.place(x=427,y=370)

DisplayBill_Delivery_fname_txt.place(x=520,y=200,width=180,height=25)
DisplayBill_Delivery_lname_txt.place(x=520,y=235,width=180,height=25)
DisplayBill_Delivery_prdname_txt.place(x=520,y=270,width=180,height=25)
DisplayBill_Delivery_deliverydate_txt.place(x=520,y=305,width=180,height=25)
DisplayBill_Delivery_pincode_txt.place(x=520,y=335,width=180,height=25)
DisplayBill_Delivery_address_txt.place(x=520,y=370,width=180,height=60)

DisplayBill_ProductDetails_prdname_lbl=Label(DisplayBillframe,text="Product Name :",font=("Tahoma",15),bg="white")
DisplayBill_ProductDetails_quantity_lbl=Label(DisplayBillframe,text="Quantity :",font=("Tahoma",15),bg="white")
DisplayBill_ProductDetails_purchasetype_lbl=Label(DisplayBillframe,text="Purchase Type :",font=("Tahoma",15),bg="white")
DisplayBill_ProductDetails_prdprice_lbl=Label(DisplayBillframe,text="Product Price :",font=("Tahoma",15),bg="white")

DisplayBill_ProductDetails_prdname_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_ProductDetails_quantity_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_ProductDetails_purchasetype_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_ProductDetails_prdprice_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)

DisplayBill_ProductDetails_prdname_lbl.place(x=30,y=500)
DisplayBill_ProductDetails_quantity_lbl.place(x=80,y=535)
DisplayBill_ProductDetails_purchasetype_lbl.place(x=27,y=570)
DisplayBill_ProductDetails_prdprice_lbl.place(x=40,y=605)

DisplayBill_ProductDetails_prdname_txt.place(x=180,y=505,width=180,height=25)
DisplayBill_ProductDetails_quantity_txt.place(x=180,y=540,width=180,height=25)
DisplayBill_ProductDetails_purchasetype_txt.place(x=180,y=575,width=180,height=25)
DisplayBill_ProductDetails_prdprice_txt.place(x=180,y=610,width=180,height=25)

DisplayBill_PricingDetails_quantity_lbl=Label(DisplayBillframe,text="Quantity :",font=("Tahoma",15),bg="white")
DisplayBill_PricingDetails_productprice_lbl=Label(DisplayBillframe,text="Product Price :",font=("Tahoma",15),bg="white")
DisplayBill_PricingDetails_totalprice_lbl=Label(DisplayBillframe,text="Total Price :",font=("Tahoma",15),bg="white")

DisplayBill_PricingDetails_quantity_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_PricingDetails_productprice_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)
DisplayBill_PricingDetails_totalprice_txt=Entry(DisplayBillframe,font=("Calibri",12),bg="lightgrey",bd=2)

DisplayBill_PricingDetails_quantity_lbl.place(x=420,y=500)
DisplayBill_PricingDetails_productprice_lbl.place(x=380,y=535)
DisplayBill_PricingDetails_totalprice_lbl.place(x=400,y=570)

DisplayBill_PricingDetails_quantity_txt.place(x=520,y=505,width=180,height=25)
DisplayBill_PricingDetails_productprice_txt.place(x=520,y=540,width=180,height=25)
DisplayBill_PricingDetails_totalprice_txt.place(x=520,y=575,width=180,height=25)

DisplayBill_Finish_btn=Button(DisplayBillframe,text="Finish",bg="yellow",fg="red",font=("Calibri",15,"bold"),cursor="hand2",command=Finish)
DisplayBill_Finish_btn.place(x=620,y=615,width=110,height=30)

#==================
window.mainloop() 
#==================