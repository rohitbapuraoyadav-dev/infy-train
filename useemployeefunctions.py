from employeewithfunctions import Manager ,Salesman ,Employee

Employee()
try:
    Salesman ("",4000,500)
except AttributeError:
    print("name cannot be blank")

try:
    Salesman("Jhon",0,500)
except ValueError:
    print("Salary cannot be zero")

try:
    Manager("Rohan",20000,-5000)
except ValueError:
    print("Perks cannot be negative")

try:
    Salesman("Jhon",50000,-595)
except ValueError:
    print("Commission cannot be a negative value")

