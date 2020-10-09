#Method Overloading
class Adding:
       
       def add(self,a=None,b=None,c=None):
              if a!=None and b!=None and c!=None:
                     return a+b+c
              elif a!=None and b!=None:
                     return a+b
              elif a!=None:
                     return a
              else:
                     return None
obj=Adding()
print(obj.add(1,2,3))
print(obj.add(1,2))
print(obj.add(1))
#print(obj.add(1,2,3,4))
print(obj.add())
              
