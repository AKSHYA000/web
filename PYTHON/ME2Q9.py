"""
Write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same. 
"""
li = ['nepal','china','bob','pop','ramesh']
count = 0
for i in li:
    if len(i)>=2 and i[0] == i[len(i)-1]:
        count += 1
print('count =',count)