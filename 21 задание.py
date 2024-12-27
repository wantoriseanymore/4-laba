# №1 Программа выведет True и затем False
# class Student:
#   pass

# class Employee:
#   pass

# employee = Employee()
# print(isinstance(employee, Employee))
# print(isinstance(employee,Student))

#№2
class Student:
  name = None

  def __init__(self,name):
    self.name = name

class Employee:
  name = None

  def __init__(self,name):
    self.name = name


users = [
	 Student('user1'),
	 Employee('user2'),
	 Student('user3'),
	 Employee('user4'),
	 Student('user5'),
	 Employee('user6'),
	 Student('user7'),
]
for employee in users:
    if isinstance(employee,Employee):
        print(employee.name)