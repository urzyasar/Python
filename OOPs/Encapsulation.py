#Encapsulation

class Bike:
       def __init__(self,n):
              self.name=n
              self.__price=50,000 #private variable
       def setprice(self,p):
              self.__price=p
              print(self.__price)
              self.__display()

       def __display(self):
              print("Bike:{} and price:{}".format(self.name,self.__price))

       def getdisplay(self):
              self.__display()
              

obj=Bike("yamaha")
#print(obj.price) #cannot access from outside
#print(obj.__price)
#print(obj.name)

#trying to set price
obj.name="honda"
print(obj.name)
#obj.__price=100
obj.setprice(10000)
#print(obj.__price) #Again it cannot access from outside

#obj.__display() #cannot access this method from outside
obj.getdisplay()
