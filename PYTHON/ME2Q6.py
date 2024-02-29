"""
Python program to find common elements in three lists using sets
"""
li1 = [1,2,3,4,5,6,7,8]
li2 = [3,2,1,0,-1,-2]
li3 = [1,3,5,7,8,11]
li1, li2, li3 = set(li1), set(li2), set(li3)
print('Common Items:')
for i in li1.intersection(li2,li3):
    print(i)