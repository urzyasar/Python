#abstraction
from abc import ABC,abstractmethod
class Food(ABC):
       @abstractmethod
       def price(self):
              pass
       @abstractmethod
       def type(self):
              pass
       def product(self):
              print("Briyani")
class Briyani(Food):
       def price(self):  #MUST DECLARE OR ELSE ERROR
            print("$100 price")
       def type(self):
              print("Non-veg")
       def product(self):    #IF WE SPECIFY THIS METHOD IT WILL OVERIRDE THE ABSTRACT CLASS METHOD #WE DONT NEED TO NECEESSARILY INCLUDE THIS METHOD
              print("Mutton Briyani")
customer1=Briyani()
customer1.price()
customer1.type()
customer1.product()
"""f1=Food()""" #CANNOT INTANIATE OBJECT FOR ABSTRACT CLASS
