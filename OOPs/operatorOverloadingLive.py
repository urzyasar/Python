#operator overloading
class Addition:
       def __init__(self,x,y):
              self.m1=x
              self.m2=y
       def __add__(self,other):
              mark1=self.m1+other.m1
              mark2=self.m2+other.m2
              avg1=mark1/2
              avg2=mark2/2
              print("Avg of student1:{} and Avg of student2: {}".format(avg1,avg2))
       def __mul__(self,other):
              mark1=self.m1*other.m1
              mark2=self.m2*other.m2
              print("Multiply:",mark1,mark2)
       
std1=Addition(100,80)
std2=Addition(100,30)
std1+std2
std1*std2

