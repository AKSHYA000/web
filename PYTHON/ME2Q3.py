"""
Write a Python program to print the numbers of a specified list after removing even numbers from it. 
"""
lis = [1,2,3,4,5,6,7,8,9,10]
print('Original list :',lis)
for i in lis:
    if i%2 == 0:
        lis.remove(i)
print('Modified List :',lis)