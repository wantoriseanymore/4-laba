class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary
	
    def show(self):
        return self.name
        
    def sal(self):
        return self.salary
   
    def proc(self):
        return self.salary + (self.salary / 100)*10
   
user = Employee('Romanov', 300)

user.show()
user.sal()
user.proc()
print(user.show())
print(user.sal())
print(user.proc())

    
    
    
    
