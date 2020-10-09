class Student:
    #class variable or static variable
    school="Matric School"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #creating Instance method
    #Because we use self or we pass the object
    def age1(self):
        if self.age<=18:
            print("child")
        else:
            print("Adult")

    #declare class method
    #this method is something common for all and it specifically for class variables
    @classmethod
    def getSchool(cls):
        return cls.school

    #declare a static method
    #There is no self and no class so it is a static method
    @staticmethod
    def info():
        print("I am a student")




#object creation
s1=Student("yasar",21)
s2=Student("arafath",20)

#To see the object address
# print(id(s1))

s2.age1()

#print(Student.getSchool(Student))
#to avoid like these we use decorators @class method
print(Student.getSchool())


s1.info()


