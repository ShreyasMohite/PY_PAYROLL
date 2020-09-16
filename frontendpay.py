#frontEnd
from tkinter import *
import tkinter.messagebox
import time
from tkinter.ttk import Combobox
import backendpay
#=====================time======================
localtime=time.asctime(time.localtime(time.time()))
#==========================================

#====================================================

     

class Employee:
     def __init__(self,root):
       self.root=root
       self.root.iconbitmap('hand.ico')
       self.root.geometry('1400x750+0+0')
       self.root.title('payroll management system')

       name=StringVar( )
       address=StringVar( )                                           
       age=StringVar( )
       DOB=StringVar( )
       Department=StringVar( )
       Eid=StringVar( )
       hourswork=IntVar( )
       overtime=StringVar( )
       salary=StringVar( )
       salary_advance=StringVar( )
       absent=StringVar( )
       netsal=StringVar( )
       joinday=StringVar( )
       mobile=StringVar( )
       Gender=StringVar( )
       #========================function================================
       def iExit( ):
            iExit=tkinter.messagebox.askyesnocancel("payroll management system","confirm if you want to exit")
            if iExit ==True:
                 root.destroy()
                 return
       def cleardata( ):
           self.name.delete(0,END)
           self.txtEmployee_Address.delete(0,END)
           self.txtEmployee_Age.delete(0,END)
           self.txtDate_Of_Birth.delete(0,END)
           self.txtcombo.delete(0,END)
           self.txtEmployee_ID.delete(0,END)
           self.txtWorks_Hours_Of_Month.delete(0,END)
           self.txtNo_Of_Monthly_Overtime.delete(0,END)
           self.txtSalary.delete(0,END)
           self.txtSalary_Advance.delete(0,END)
           self.txtAbsent_Day_Of_Month.delete(0,END)
           self.txtnetsal.delete(0,END)
           self.txtJONING_DAY.delete(0,END)
           self.txtMOBILE_NUMBER.delete(0,END)
           self.txtGENDER.delete(0,END)
           self.txtpayment_slip.delete("1.0",END)

       def salC( ):
          """sla=float(self.txtSalary.get( ))
          HRA=sla *  0.15
          DA=sla * 0.08
          PF=sla * 0.05
          I_tax=sla * 0.08
          grosspay=sla + HRA +DA
          deduction=I_tax +PF
          pay=grosspay -  deduction
          NETSALARY="$",str ('%.2f' % (pay))
          netsal.set(NETSALARY)
          return """
          ab=int(self.txtWorks_Hours_Of_Month.get())
          bc=int(self.txtSalary_Advance.get())
          if ab>200 & ab<240:
               sal=ab*50
               salary.set(sal)
               HRA=sal *  0.15
               DA=sal * 0.08
               PF=sal * 0.05
               I_tax=sal * 0.08
               grosspay=sal + HRA +DA
               deduction=I_tax +PF-bc
               pay=grosspay -  deduction
               NETSALARY="Rs",str ('%.2f' % (pay))
               netsal.set(NETSALARY)
               absent.set(7)
          elif ab>240 & ab<300:
               sal=ab*50
               salary.set(sal)
               HRA=sal *  0.15
               DA=sal * 0.08
               PF=sal * 0.05
               I_tax=sal * 0.08
               grosspay=sal + HRA +DA
               deduction=I_tax +PF-bc
               pay=grosspay -  deduction
               NETSALARY="Rs",str ('%.2f' % (pay))
               netsal.set(NETSALARY)
               absent.set(0)
          elif ab>300 & ab<360:
               sal=ab*50
               salary.set(sal)
               HRA=sal *  0.15
               DA=sal * 0.08
               PF=sal * 0.05
               I_tax=sal * 0.08
               grosspay=sal + HRA +DA
               deduction=I_tax +PF-bc
               pay=grosspay -  deduction
               NETSALARY="Rs",str ('%.2f' % (pay))
               netsal.set(NETSALARY)
               absent.set(0)
               overtime.set(3)
          elif ab>360 & ab<420:
               sal=ab*50
               salary.set(sal)
               HRA=sal *  0.15
               DA=sal * 0.08
               PF=sal * 0.05
               I_tax=sal * 0.08
               grosspay=sal + HRA +DA
               deduction=I_tax +PF-bc
               pay=grosspay -  deduction
               NETSALARY="Rs",str ('%.2f' % (pay))
               netsal.set(NETSALARY)
               absent.set(0)
               overtime.set(3)
               
          else:
               pass
               
          
          
       def Enterinfo( ):
           self.txtpayment_slip.insert(END,"\t\tPayment Slip\n\n")
           self.txtpayment_slip.insert(END,'Employee_ID:  \t\t' + self.txtEmployee_ID.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'Name:  \t\t' + self.name.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'Age:  \t\t' +  self.txtEmployee_Age.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'Address:  \t\t' + self.txtEmployee_Address.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'Department:  \t\t' +  self.txtcombo.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'Hours work:  \t\t' +  self.txtWorks_Hours_Of_Month.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'Overtime:  \t\t' + self.txtNo_Of_Monthly_Overtime.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'Salary_Advance:  \t\t' + self.txtSalary_Advance.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'Salary:  \t\t' +self.txtSalary.get( ) + "\n\n")
           self.txtpayment_slip.insert(END,'NETSALARY:  \t\t' + self.txtnetsal.get( ) + "\n\n")
          

       def adddata( ):
           if(len(Eid.get( )) !=0):
                backendpay.addemprec(Eid.get( ),name.get( ),age.get( ),address.get( ),DOB.get( ),salary.get( ),netsal.get(),Gender.get(),mobile.get())
                emplist.delete(0,END)
                emplist.insert(END,(Eid.get( ),name.get( ),age.get( ),address.get( ),DOB.get( ),salary.get( ),netsal.get(),Gender.get(),mobile.get( )))
                      
       def display( ):
                  emplist.delete(0,END)
                  for rows in backendpay.viewdata( ):
                       emplist.insert(END,rows,str(""))

       def employeerec(event):
            global sd
            serachemp=emplist.curselection( )[0]
            sd=emplist.get(serachemp)
            self.txtEmployee_ID.delete(0,END)
            self.txtEmployee_ID.insert(END,sd[1])
            self.name.delete(0,END)
            self.name.insert(END,sd[2])
            self.txtEmployee_Age.delete(0,END)
            self.txtEmployee_Age.insert(END,sd[3])
            self.txtEmployee_Address.delete(0,END)
            self.txtEmployee_Address.insert(END,sd[4])
            self.txtDate_Of_Birth.delete(0,END)
            self.txtDate_Of_Birth.insert(END,sd[5])
            self.txtSalary.delete(0,END)
            self.txtSalary.insert(END,sd[6])
            self.txtnetsal.delete(0,END)
            self.txtnetsal.insert(END,sd[7])
            self.txtGENDER.delete(0,END)
            self.txtGENDER.insert(END,sd[8])
            self.txtMOBILE_NUMBER.delete(0,END)
            self.txtMOBILE_NUMBER.insert(END,sd[9])
            
       def delete( ):
           if(len(Eid.get( ) ) !=0):
                backendpay.deleterec(sd [0])
                cleardata( )
                display( )

       def searchdata( ):
             emplist.delete(0,END)
             for rows in backend.paySearch(Eid.get( ),name.get( ),age.get( ),address.get( ),DOB.get( ),salary.get( ),netsal.get( ),Gender.get( ),mobile.get( )):
                  emplist.insert(END,rows,str(" "))


       def updatedata( ):
            if(len(Eid.get( ) )!=0):
                 backendpay.deleterec(sd[0])
            if(len(Eid.get( ) )!=0):
                   backendpay.addemprec(Eid.get( ),name.get( ),age.get( ),address.get( ),DOB.get( ),salary.get( ),netsal.get(),Gender.get(),mobile.get())
                   emplist.delete(0,END)
                   emplist.insert(END,Eid.get( ),name.get( ),age.get( ),address.get( ),DOB.get( ),salary.get( ),netsal.get(),Gender.get(),mobile.get())
                  
                 
            
                       
                     
                
                
          
           
           
       salary_advance.set(0)
            
       
       #========================frame================================
       frame=Frame(self.root,height=50,width=1350,bd=8,relief='raise',bg='cornsilk4')
       frame.pack(side=TOP)
       f1=Frame(self.root,height=600,width=600,bd=8,relief='raise',bg='powder blue')
       f1.pack(side=LEFT)
       f2=Frame(self.root,height=700,width=300,bd=8,relief='raise',bg='gray',pady=10)
       f2.pack(side=RIGHT)
       f3=Frame(f1,height=200,width=600,bd=20,relief='raise')
       f3.pack(side=TOP)
       f4=Frame(f1,height=600,width=600,bd=20,relief='groove')
       f4.pack(side=TOP)
       #=================lables=====================================
       self.lab=Label(frame,font=('arial',40,'bold'),text="                  payroll    management   system                  ",fg='steel blue3',bd=5);
       self.lab.grid(row=0,column=0)
       self.lab2=Label(frame,font=('arial',10),text=localtime,fg='steel blue').grid(row=1,column=0)
       self.Employee_ID=Label(f3,font=('arial',10,'bold'),text="Employee_ID",fg='steel blue4',bd=8).grid(row=0,column=0)                
       self.name=Label(f3,font=('arial',10,'bold'),text="Employee_NAME",fg='steel blue4',bd=8).grid(row=0,column=2)
       self.Employee_Age=Label(f3,font=('arial',10,'bold'),text="Employee_Age",fg='steel blue4',bd=8).grid(row=1,column=0)
       self.Date_Of_Birth=Label(f3,font=('arial',10,'bold'),text="Date_Of_Birth",fg='steel blue4',bd=8).grid(row=1,column=2)
       self.Department=Label(f3,font=('arial',10,'bold'),text="Department",fg='steel blue4',bd=8).grid(row=2,column=0)
       self.Employee_Address=Label(f3,font=('arial',10,'bold'),text="Employee_Address",fg='steel blue4',bd=8).grid(row=2,column=2)
       self.Works_Hours_Of_Month=Label(f3,font=('arial',10,'bold'),text="Works_Hours",fg='steel blue4',bd=8).grid(row=3,column=0)
       self.No_Of_Monthly_Overtime=Label(f3,font=('arial',10,'bold'),text="Monthly_Overtime",fg='steel blue4',bd=8).grid(row=3,column=2)
       self.Salary=Label(f3,font=('arial',10,'bold'),text="Salary",fg='steel blue4',bd=8).grid(row=4,column=0)
       self.Salary_Advance=Label(f3,font=('arial',10,'bold'),text="Salary_Advance",fg='steel blue4',bd=8).grid(row=4,column=2)
       self.Absent_Day_Of_Month=Label(f3,font=('arial',10,'bold'),text="Absent_Days",fg='steel blue4',bd=8).grid(row=5,column=0)
       self.txtnetsal=Label(f3,font=('arial',10,'bold'),text="NET_SALARY",fg='steel blue4',bd=8).grid(row=5,column=2)
       self.JONING_DAY=Label(f3,font=('arial',10,'bold'),text="Gender",fg='steel blue4',bd=8).grid(row=6,column=0)
       self.MOBILE_NUMBER=Label(f3,font=('arial',10,'bold'),text="JONING_DAY",fg='steel blue4',bd=8).grid(row=6,column=2)
       self.GENDER=Label(f3,font=('arial',10,'bold'),text="MOBILE_NUMBER",fg='steel blue4',bd=8).grid(row=7,column=2)

       #=======================Entry widget==================================
       #self.txtEmployee_ID=Entry(f3,textvariable=Eid,bd=16,font=('arial',12,'bold'),width=22,justify=RIGHT)  
       #self.txtEmployee_ID.grid(row=0,column=1)
       v=list(range(120010,120090))
       self.txtEmployee_ID=Combobox(f3,values=v,font=('arial',10),width=25,textvariable=Eid,state="readonly")
       self.txtEmployee_ID.grid(row=0,column=1)
       self.txtEmployee_ID.set("select ID")
       self.name=Entry(f3,textvariable=name,bd=16,font=('arial',12,'bold'),width=22,justify=RIGHT)
       self.name.grid(row=0,column=3)
       #self.txtEmployee_Age=Entry(f3,textvariable=age,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)          #Eid.get(),name.get() ,age.get() ,address.get() ,DOB.get() ,Department.get() ,hours_work.get() ,overtime.get() ,salary.get() ,salary_advance.get() ,\                                                                                                                                                                         #absent.get() ,NETSALARY.get() ,Gender.get() ,joinday.get() ,mobile.get()
       #self.txtEmployee_Age.grid(row=1,column=1)
       v=list(range(18,75))
       self.txtEmployee_Age=Combobox(f3,values=v,font=('arial',10),width=25,textvariable=age,state="readonly")
       self.txtEmployee_Age.grid(row=1,column=1)
       self.txtEmployee_Age.set("select age")
       self.txtDate_Of_Birth=Entry(f3,textvariable=DOB,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtDate_Of_Birth.grid(row=1,column=3)
       """v=list(range(1,32))
       self.txtDate_Of_Birth=Combobox(f3,values=v,font=('arial',8),width=5)
       self.txtDate_Of_Birth.set("Day")
       self.txtDate_Of_Birth.grid(row=1,column=3)
       v=list(range(1,13))
       self.txtDate_Of_Birth=Combobox(f3,values=v,font=('arial',8),width=5)
       self.txtDate_Of_Birth.set("Month")
       self.txtDate_Of_Birth.grid(row=1,column=4)
       v=list(range(1980,2025))
       self.txtDate_Of_Birth=Combobox(f3,values=v,font=('arial',8),width=5)
       self.txtDate_Of_Birth.set("Year")
       self.txtDate_Of_Birth.grid(row=1,column=5)"""
       #self.txtDepartment=Entry(f3,textvariable=Department,bd=16,font=('arial',12,'bold'),width=22,justify=RIGHT)
       #self.txtDepartment.grid(row=2,column=1)
       v=["IT","C.S","S.D"]
       self.txtcombo=Combobox(f3,textvariable=Department,values=v,font=('arial',10),width=25,state="readonly")
       self.txtcombo.grid(row=2,column=1)
       self.txtcombo.set("select Department")
       self.txtEmployee_Address=Entry(f3,textvariable=address,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtEmployee_Address.grid(row=2,column=3)
       #self.txtWorks_Hours_Of_Month=Entry(f3,textvariable=hours_work,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       #self.txtWorks_Hours_Of_Month.grid(row=3,column=1)
       b=list(range(200,420))
       self.txtWorks_Hours_Of_Month=Combobox(f3,textvariable=hourswork,values=b,font=('arial',10),width=25,state="readonly")
       self.txtWorks_Hours_Of_Month.grid(row=3,column=1)
       self.txtWorks_Hours_Of_Month.set("select hours")
       
       self.txtNo_Of_Monthly_Overtime=Entry(f3,textvariable=overtime,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtNo_Of_Monthly_Overtime.grid(row=3,column=3)
       self.txtSalary=Entry(f3,textvariable=salary,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtSalary.grid(row=4,column=1)
       self.txtSalary_Advance=Entry(f3,textvariable=salary_advance,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtSalary_Advance.grid(row=4,column=3)
       self.txtAbsent_Day_Of_Month=Entry(f3,textvariable=absent,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtAbsent_Day_Of_Month.grid(row=5,column=1)
       self.txtnetsal=Entry(f3,textvariable=netsal,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtnetsal.grid(row=5,column=3)
       self.txtJONING_DAY=Entry(f3,textvariable=joinday,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtJONING_DAY.grid(row=6,column=3)
       self.txtMOBILE_NUMBER=Entry(f3,textvariable=mobile,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       self.txtMOBILE_NUMBER.grid(row=7,column=3)
       #self.txtGENDER=Entry(f3,textvariable=Gender,bd=16,font=('arial',12,'bold'),width=22,justify=LEFT)
       #self.txtGENDER.grid(row=6,column=1)
       v=["Male","Female","Trans"]
       self.txtGENDER=Combobox(f3,values=v,font=('arial',10),width=25,textvariable=Gender,state="readonly")
       self.txtGENDER.grid(row=6,column=1)
       self.txtGENDER.set("select Gender")
       #=========================payment_slip=======================
       lab=Label(f2,font=('arial',10,'bold'),text="Employee_Payment",fg='peachpuff4').grid(row=0,column=0)
       self.txtpayment_slip=Text(f2, width=70,height=20,font=('arial',8,'bold'),bd=10,state="normal")
       self.txtpayment_slip.grid(row=1,column=0)
       lab=Label(f2,font=('arial',10,'bold'),text="Search_Employee",fg='peachpuff4').grid(row=2,column=0)
       #========================buttons===========================
       but1=Button(f4,text='Add New',command= adddata,bg='light cyan',bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=1)
       lab=Label(f4).grid(row=0,column=2)
       but2=Button(f4,text='Display',bg='light cyan',command= display,bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=3)
       lab=Label(f4).grid(row=0,column=4)
       but3=Button(f4,text='Clear',command=cleardata,bg='light cyan',bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=5)
       lab=Label(f4).grid(row=0,column=6)
       but3=Button(f4,text='Delete',command=delete,bg='light cyan',bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=7)
       lab=Label(f4).grid(row=0,column=8)
       but4=Button(f4,text='Search',bg='light cyan',command=searchdata,bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=9)
       lab=Label(f4).grid(row=0,column=10)
       but5=Button(f4,text='Update',bg='light cyan',command=updatedata,bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=11)
       lab=Label(f4).grid(row=0,column=12)
       but6=Button(f4,text='pay_slip',bg='light cyan',command= Enterinfo,bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=13)
       lab=Label(f4).grid(row=0,column=14)
       but7=Button(f4,text='total_salary',bg='light cyan',command=salC,bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=15)
       lab=Label(f4).grid(row=0,column=16)
       but8=Button(f4,text='Exit',command= iExit,bg='light cyan',bd=8,height=3,width=8,font=('arial',8,'bold')).grid(row=0,column=17)
       
       #======================================scrollbar & listbox====================================
       """y axis bar"""
       scrollbar=Scrollbar(f2)
       scrollbar.grid(row=3,column=1)
       """x axis bar"""
       sor=Scrollbar(f2,orient=HORIZONTAL)
       sor.grid(row=10,column=0)
       emplist=Listbox(f2,height=11,width=80,bd=10,yscrollcommand=scrollbar.set,xscrollcommand=sor.set)
       emplist.bind('<<ListboxSelect>>',employeerec)

      

       
       
       #emplist.bind('<<ListboxSelect>>',employeerec)
       emplist.grid(row=3,column=0)
       scrollbar.config(command=emplist.yview)
       sor.config(command=emplist.xview)
       
       
     

       
       

       
       




       
if __name__=='__main__':
     root=Tk()
     application=Employee(root)
     root.mainloop()
