class CE:
    def __init__(self,rollno,section):
        self.rollno=rollno
        self.section=section 
    def abc(self):
        z=self.section+30
        print(z)   
aman=CE(1,2)
aman.rollno=10
aman.section=2
print(aman.rollno,aman.section)
aman.abc()