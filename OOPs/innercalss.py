#inner class Example
class Student:
       def __init__(self,name,roll):
              self.name=name
              self.roll=roll
              self.lap=self.Laptop()

       def show(self):
              return self.name,self.roll,self.lap.show()

       class Laptop:
              def __init__(self):
                     self.brand="hp"
                     self.cpu='i3'
                     self.ram=4
              def show(self):
                     return self.brand,self.cpu,self.ram

s1=Student("yasar","17IT053")
print(s1.show())
print(s1.lap.show())
