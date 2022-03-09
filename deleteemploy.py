import sqlite3

connection = sqlite3.connect("company.db")

getcode = input("enter the employee code: ")

connection.execute("delete from Employee where employeecode="+getcode)
connection.commit()

print("Data deleted successfully")

result = connection.execute("select * from Employee")

print("Employee data updated")

for i in result:
    print("code =>",i[0])
    print("employeename =>",i[1])
    print("designation =>",i[2])
    print("salary =>",i[3])
    print("companyname =>",i[4])
    print("mobilenumber =>",i[5])
