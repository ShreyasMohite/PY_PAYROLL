import sqlite3
#backend

def Employeedata( ):
     con=sqlite3.connect("employee.db")
     cur=con.cursor(  )
     cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY,Eid text,name text,age text,address text,DOB text,salary text,netsal text,Gender text,mobile text)")
     con.commit( )
     con.close( )
     
def addemprec(Eid,name ,age ,address ,DOB ,salary ,netsal ,Gender,mobile):                  
     con=sqlite3.connect("employee.db")                                                                                                                           
     cur=con.cursor( )
     cur.execute("INSERT INTO employee VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(Eid,name ,age ,address ,DOB ,salary ,netsal ,Gender,mobile))
     con.commit( )
     con.close

def viewdata( ):
     con=sqlite3.connect("employee.db")                                                                                                                           
     cur=con.cursor(  )
     cur.execute("SELECT * FROM employee ")
     rows=cur.fetchall( )
     con.close( )
     return rows

def deleterec(id ):
     con=sqlite3.connect("employee.db")                                                                                                                           
     cur=con.cursor(  )
     cur.execute("DELETE  FROM employee WHERE id=?",  (id,) )
     con.commit( )
     con.close( )
def Search(Eid=" ",name= " " ,age= " " ,address= " " ,DOB="  " ,salary=" "  ,netsal=" " ,Gender=" " ,mobile=" " ):
     con=sqlite3.connect("employee.db")
     cur=con.cursor(  )
     cur.execute("SELECT * FROM employee WHERE Eid=? OR name=? OR age=? OR address=? OR DOB=? OR salary=? OR netsal=? OR Gender=? OR mobile=? ",
                 (Eid,name ,age ,address ,DOB ,salary ,netsal ,Gender ,mobile))
     rows=cur.fetchall( )
     con.close( )
     return rows

def update(id,Eid=" ",name=" "  ,age=" "  ,address=" " ,DOB=" " ,salary=" "  ,netsal=" "  ,Gender=" " ,mobile=" "):
     con=sqlite3.connect("employee.db")
     cur=con.cursor(  )
     cur.execute("SELECT * FROM employee WHERE Eid=? ,name=? , age=? , address=? ,DOB=? , salary=? , netsal=? ,Gender=?  , mobile=?",
                 (Eid,name ,age ,address ,DOB  ,salary ,netsal ,Gender  ,mobile,id))
     con.commit( )
     con.close( )

Employeedata( )

     
