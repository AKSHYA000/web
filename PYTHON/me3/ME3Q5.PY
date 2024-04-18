"""
Write a Python program to Employee Management System:
Define an Employee class to represent employees. It can include attributes like name, 
employee ID, salary, etc. Methods can be implemented for giving raises, displaying employee 
details, etc.
"""
employees = []
class Employee:
    def __init__(self):
        self.name = input('Enter employee Name : ')
        self.ID = int(input('Enter employee ID : '))
        self.sal = int(input('Enter employee Salary : '))
    def raise_salary(self,amount):
        if amount>0:
            self.sal += amount
        else:
            print('ERROR')
    def display_info(self):
        print('Employee ID :',self.ID)
        print('Employee Name :',self.name)
        print('Employee Salary :',self.sal)
def get_employee_by_id():
    id = int(input('Enter Employee ID : '))
    for i in employees:
        if i.ID == id:
            return i
while True:
    option = int(input('\n1.Add Employee\n2.Raise Salary\n3.Display EMployee Info\n*.Exit\nchoice = '))
    if option == 1:
        emp = Employee()
        employees.append(emp)
    elif option == 2:
        emp = get_employee_by_id()
        if emp:
            amount = int(input('ENter amount of raise : '))
            emp.raise_salary(amount)
            print('Salary Raised Sucessfully')
        else:
            print('ERR')
    elif option == 3:
        emp = get_employee_by_id()
        if emp:
            emp.display_info()
        else:
            print('ERR')
    else:
        print('ERR')
        break