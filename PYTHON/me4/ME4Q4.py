"""
Write a program to Implement  hybrid inheritance to manage student Information System.
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class citizen(Person):
    def __init__(self,name, age, country, state):
        self.country = country
        self.state = state
        Person.__init__(self,name,age)
class Personal_info:
    def __init__(self,phone,email):
        self.phone = phone
        self.email = email
class Student(citizen, Personal_info):
    def __init__(self):
        data = self.get_data()
        citizen.__init__(self,data[0],data[1],data[2],data[3])
        Personal_info.__init__(self, data[4], data[5])
    @staticmethod
    def get_data():
        data = []
        data.append(input('Student Name : '))
        data.append(input('Student Age : '))
        data.append(input('Student country : '))
        data.append(input('Student state : '))
        data.append(input('Student phone no : '))
        data.append(input('Student email : '))
        return data
    def show_data(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Country : {self.country}')
        print(f'State : {self.state}')
        print(f'Phone no : {self.phone}')
        print(f'Email : {self.email}')
obj = Student()
obj.show_data()