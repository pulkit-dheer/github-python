## Q1

eno = int(input("Enter Employee Number: "))
ename = input("Enter Employee Name: ")
esal = float(input("Enter Employee Salary: "))
eaddr = input("Enter Employee Address: ")
married = eval(input("Is Employee Married?[True|False]: "))

print('Please confirm your provided information')
print('Employee Number: ', eno)
print('Employee Name: ', ename)
print('Employee Salary: ', esal)
print('Employee Address: ', eaddr)
print('Employee Married: ', married)


#Q2 

a,b = [int(x) for x in input("Enter 2 numbers: ").split()]
print("The sum is: ", a+b)