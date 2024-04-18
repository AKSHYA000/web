"""
Write a python program to implement Student Management System:
Create a Student class to represent students. Each student has attributes like name, 
roll number, and marks. You can have methods to calculate the average marks, display student 
details, etc.
"""
class student:
    subjects = ('Math','Science','Computer','English','Social')
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.marks = self.marks_input()
    def calculate_average(self):
        total_sum = 0
        for i in self.marks:
            total_sum += i
        return total_sum/len(self.marks)
    def display_info(self):
        print('Student Name :',self.name)
        print('Student Roll :',self.roll)
        print('Student Marks :')
        for i in range(len(self.subjects)):
            print('\t',i+1,self.subjects[i],'=',self.marks[i])
        print('Average Marks = ',self.calculate_average())
    def marks_input(self):
        mark = []
        print('')
        for i in range(len(self.subjects)):
            m = int(input(f'{i+1}.{self.subjects[i]} = '))
            mark.append(m)
        return mark
studentName = input('Enter Student Name : ')
studentRoll = int(input('Enter Student Roll no : '))
studentObject = student(studentName,studentRoll)
studentObject.display_info()