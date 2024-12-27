class Employee:
    __name = None
    __age = None
    __salary = None

    def __init__(self,name,age,salary):
        self.__name = name 
        self.__age = age
        self.__salary = salary

    def getName(self):
        return self.__name 
	
    def getAge(self):
        return self.__age

    def getSalary(self):
        return self.__salary
    
    def setName(self,name):
       self.__name = name

    def setAge(self,age):
        self.__age = age
    
    def setSalary(self,salary):
        self.__salary = salary
   
    
user = Employee('', '', '')

user.setName('Roubassow')
user.setAge('17')
user.setSalary('3500')
print(user.getName()) 
print(user.getAge())
print(user.getSalary())
