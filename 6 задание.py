class Emoloyee:
    def show(self, name, salary):
        return name + ' - ' + salary
  
user = Emoloyee()
user.show('Romanov', '300 тенге ')
print(user.show('Romanov', '300 тенге '))