class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

 	def getSalary(self):
		return self.addSign(self.salary)


	def addSign(self,num):
		return num + '$'

	
user = User('john')
print(user.show())
