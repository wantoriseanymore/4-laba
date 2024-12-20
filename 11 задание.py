class Employee:
    name = None
    salary = None
    
    def _init_(self, name, salary):
        print(name + ' - ' + salary)
    
employee = Employee()
employee._init_('Romanov', '300 тенге')
