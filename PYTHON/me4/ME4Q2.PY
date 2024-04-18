class Shape:
    def area():
      pass
class Rectangle(Shape):
    def __init__(self,length,bredth):
      self.length=length
      self.bredth=bredth
    
    def area(self):
        s = self.length*self.bredth 
        print (s)

class Circle(Shape):
    def __init__(self,radius):
      self.radius= radius
    
    def area(self):
        s= 22/7*self.radius*self.radius
        print (s)

length=int(input("entre length="))
bredth=int(input("entre bredth=")) 
radius=int(input("entre radius="))   

a=Rectangle(length,bredth)
a.area()

b=Circle(radius)
b.area()



        
   
