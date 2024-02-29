


"""lambda"""
num=[1,2,3,4,5,6,7,8,9,33]
even=list(filter(lambda n:n%2==0,num))
print(even)
"""mapping"""
def operation(n):
    return n*n
e=list(map(lambda n:n*n,even))
print(e)
"""reduce"""
from functools import reduce
def ad(x,y):
       return x+y
e=reduce(ad,even)
print(e)

