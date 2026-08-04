from employeefn import Salesman
from addrs import Address
from dept import Department

deptobj = Department("Sales", "Mumbai") 
addressobj = Address("Jerbai Road", "Mumbai", 400012)

try:
    salary = -1000

    if salary <= 0:
        raise ValueError("Salary cannot be zero")

except ValueError as e:
    print("Value Error :", e)

try:
    s1 = Salesman("", 4000, 500, deptobj, addressobj)

except Exception as e:
    print("Exception occurred:", e)


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
