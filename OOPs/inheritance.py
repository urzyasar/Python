#Inheritance
class Bank:
       def __init__(self,id,name,age,ac_no):
              self.id=id
              self.name=name
              self.age=age
              self.ac_no=ac_no
       def display(self):
              print(" ID:",self.id,"\n","Name:",self.name,"\n","Age:",self.age,"\n","Account",self.ac_no)
"""
class Person(Bank):
       pass #specify pass if you dont want any methods and properities.
p1=Person(1,"yasar",20,123456789)
p1.display()
"""
class Person(Bank):
       def __init__(self,a,b,c,d,mob_no):
              super().__init__(a,b,c,d) #here super() function inherits methods and properities from parent class
              self.mob=mob_no
       def dis(self):
              print(self.mob)

p1=Person(1,"yasar",20,123456789,8778473397)
p1.display()
p1.dis()              
