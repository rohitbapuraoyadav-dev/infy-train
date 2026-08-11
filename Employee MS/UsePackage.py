from testpackage import Department, Address, Employee, Manager, Salesman

# Create Department object
dept = Department("IT", "Bangalore")

# Create Address object
addr = Address("MG Road", "Bangalore", "560001")

# Create Employee object
emp = Employee("Rohit", 50000, dept, addr)

# Create Manager object
mgr = Manager("Akshay", 80000, 15000, dept, addr)

# Create Salesman object
sales = Salesman("Rahul", 40000, 5000, dept, addr)

# Display details
print(emp.show_emp_details())

print("\nManager Details")
print("Manager Name :", mgr.getEmpName())
print("Total Salary :", mgr.show_total_salary())

print("\nSalesman Details")
print("Salesman Name :", sales.getEmpName())
print("Total Salary :", sales.show_total_salary())

print("\nDepartment Details")
print(dept.showDeptDetails())

print("\nAddress Details")
print(addr.showAddressDetails())