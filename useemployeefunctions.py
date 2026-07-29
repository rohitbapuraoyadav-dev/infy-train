from employeewithfunctions import *
from department import Department
from address import Address

deptobj =Department("Python Data Science", "Pune")
empobj = Employee("Ganesh",123123,deptobj)
print(empobj.show_emp_details())
print(empobj.getDeptDetails())

addressobj = Address("Jerbai Road","Mumbai",400012)
#empobj.setAddress(addressobj)
# print(empobj.getAddress())
empobj = Employee("Rohit",1234,addressobj)
print(empobj.show_emp_details())
print(empobj.getshowAddressDetails())





# Employee()
# try:
#     Salesman ("",4000,500)
# except AttributeError:
#     print("name cannot be blank")

# try:
#     Salesman("Jhon",0,500)
# except ValueError:
#     print("Salary cannot be zero")

# try:
#     Manager("Rohan",20000,-5000)
# except ValueError:
#     print("Perks cannot be negative")

# try:
#     Salesman("Jhon",50000,-595)
# except ValueError:
#     print("Commission cannot be a negative value")


