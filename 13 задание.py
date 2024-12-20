class Employee:
    __name = None
    __salary = None
    __age = None
    def __init__(self,name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def show(self):
        return self.__name + ' - ' + self.__salary + ' - ' + self.__age

employee = Employee('Romanov', '300 tenge', '17')
employee.show()
print(employee.show())