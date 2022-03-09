import sqlite3

connection = sqlite3.connect("company.db")

getemployeecode = input("enter the employeecode:")
getemployeename = input("enter the employee name :")
getdesignation = input("enter the employee designation:")
getsalary = input("enter the employee salary:")
getcompanyname = input("enter the company name:")
getmobilenumber = input("enter the mobile number:")

result = connection.execute("update Employee set employeename='"+getemployeename+"',designation='"+getdesignation+"',salary="+getsalary+",companyname='"+getcompanyname+"',mobilenumber="+getmobilenumber+" where employeecode="+getemployeecode+"")
connection.commit()

print("data updated successfully")
result = connection.execute("select * from Employee where employeecode="+getemployeecode+"")

print("data updated")

for i in result:
    print("code =>", i[0])
    print("employeename =>", i[1])
    print("salary =>", i[2])
    print("companyname =>", i[3])
    print("mobilenumber =>", i[4])

