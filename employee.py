import sqlite3

connection = sqlite3.connect("company.db")

# connection.execute(''' Create Table Employee(
#                 employeecode integer primary key autoincrement,
#                 employeename text,
#                 designation text,
#                 salary integer,
#                 companyname text,
#                 mobilenumber integer
#
# )''')

print("The table created successfully")

getemployeename = input("enter the employee name :")
getdesignation = input("enter the employee designation:")
getsalary = input("enter the employee salary:")
getcompanyname = input("enter the company name:")
getmobilenumber = input("enter the mobile number:")

connection.execute("insert into employee(employeename,designation,salary,companyname,mobilenumber) values('"+getemployeename+"','"+getdesignation+"',"+getsalary+",'"+getcompanyname+"',"+getmobilenumber+")")

connection.commit()
connection.close()

print("Inserted Successfully")