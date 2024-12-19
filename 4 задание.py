class User:
    name = None
    salary = None
    pass

user1 = User()
user2 = User()

user1.name = "Romanov"
user1.salary = 50
user2.name = "Nebledniy"
user2.salary = 69

print(user1.name)
print(user2.name)
salary = user1.salary + user2.salary
print(salary)