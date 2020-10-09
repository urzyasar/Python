#Multiple Inheritance
class Vehicle:
       def __init__(self,c,mod,yr):
              self.color=c
              self.model=mod
              self.year=yr
       def display(self):
              print(self.color)
              print(self.model)
              print(self.year)
class Bike:
       def __init__(self,p):
              self.price=p
              
class SportsBike(Vehicle,Bike):
       def __init__(self,a,b,c,d,cc):
              self.CC=cc
              Vehicle.__init__(self,a,b,c)
              Bike.__init__(self,d)
              
       def display1(self):
              print(self.color)
              print(self.model)
              print(self.year)
              print(self.price)
              print(self.CC)

p1=Vehicle("Red","Ferrari","1980")
p1.display()

p2=SportsBike("Red","Ferrari","1980","20000","200cc")
p2.display1()

print(issubclass(Bike,Vehicle))
print(issubclass(SportsBike,Vehicle))
print(issubclass(SportsBike,Bike))
