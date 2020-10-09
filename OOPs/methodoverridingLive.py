#method overriding
class Parent:
       def __init__(self):
              self.value=5
       def getValue(self):
              return self.value
class Child(Parent):
       def getValue(self,a):
              self.a=a
              return self.value+self.a
obj=Child()
print(obj.getValue(5))
