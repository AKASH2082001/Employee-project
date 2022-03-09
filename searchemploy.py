import sqlite3

connection = sqlite3.connect("company.db")

getsalary = input("enter the salary to be searched :")

result = connection.execute("select * from employee where salary="+getsalary)

for i in result:
    print("code =>", i[0])
    print("employeename =>", i[1])
    print("salary =>", i[2])
    print("companyname =>", i[3])
    print("mobilenumber =>", i[4])
