# enter salary detect 10% tax from it and then print net salary

sal=int(input("Enter Salary :"))
tax=int(input("Enter Tax  :"))
tax= sal*tax/100
print("Tax Applied : ",tax)
net_salary= sal-tax
print("net_salary",net_salary)