class Employee:
	empcount=0
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empcount+=1
	def displaycount(self):
		print("total employees%d".empcount)
	def displayemployee(self):
		print("name:",self.name,"salary:",self.salary)
emp1=Employee('zara',2000)
emp2=Employee('manni',3000)
emp1.displayemployee()
emp2.displayemployee()
