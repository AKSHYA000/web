'''	Vehicle Inheritance:
Define a class Vehicle with attributes make and model, and a method display_info() that prints 
the make and model of the vehicle.Then, create two subclasses Car and Motorcycle that inherit
 from Vehicle and add an additional attribute year to both subclasses.Override the display_info()
method in each subclass to include the year of the vehicle.'''
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def display_info(self):
        print(f"manufacture and model= ,{self.make},{self.model}")
class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year=year
    def display_info(self):
        super().display_info()
        print(f"year= {self.year}")
class Bike(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year=year
    def display_info(self):
        super().display_info()
        print(f"year= {self.year}")
s=Bike(make="YAMAHA",model="R1m",year=2023)
s.display_info()
c=Car(make="Koenigsegg",model="jesko",year=2020)
c.display_info()







