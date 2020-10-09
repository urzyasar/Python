class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def func(self):
        return "hi iam "+self.name+str(self.age)
    
#creating an object
P1=Person("yasar",21)
p2=Person("Naveen",21)



#printing the object
print(P1.name)
print(P1.age)
print(P1.func())
print(p2.func())

