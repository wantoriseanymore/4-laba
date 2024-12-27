#1
class Employee:
    __name = None

    def __init__(self,name):
        self.__name = name 
emp1 = Employee('john') 
emp2 = Employee('eric') 
print(emp1 == emp2)

#Программа  выведет False

#2 
print(emp1 == emp1)

#Программа  выведет True

#3
emp12 = Employee('john') 
emp22 = Employee('john') 
print(emp12 == emp22)

#Программа  выведет False

#4
print(emp1 != emp1) 

#Программа  выведет False

#5
print(emp1 != emp2)

#Программа  выведет True

#6
emp11 = Employee('john') 
emp22 = emp1 
emp22.name = 'eric' 

print(emp11 == emp22)

#Программа  выведет False