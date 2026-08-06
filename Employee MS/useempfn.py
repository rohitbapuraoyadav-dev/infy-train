from employeefn import Salesman,Manager
from addrs import Address
from dept import Department
import pickle

def WriteDeptObject(dept):
    with open("DeptDetails.dat","bw+") as file:
       # file.write(dept)#Type error : a byte-like object is reqd not "Department"
        pickle.dump(dept,file)

def ReadDeptObject():
    with open("DeptDetails.dat", "rb+") as file:
        deptobj=pickle.load(file)
    print("Dept Id:", deptobj.getDeptId())
    for emp in deptobj.getEmployee():
        print("Emp Details:", emp.getEmpId(),emp.getEmpName(),emp.getSalary())
      

try:

    deptobj = Department("Sales", "Mumbai") 
    addrsobj = Address("Jerbai Road", "Mumbai", "400012")

    try:
        empobj1=Manager("Mgr01",56784,2367,deptobj, addrsobj)
        empobj1.setAddress(addrsobj)
        print(empobj1.show_emp_details())

    except ValueError:
        print("Invalid values in manager")

    try:
        empobj2=Salesman("Crk01",43567,654456,deptobj,addrsobj)
        empobj2.setAddress(addrsobj)
        print(empobj2.show_emp_details())
    except ValueError:
        print("Invalid vales in Salesman.")
    emp=set()#set of employees 
    emp.add(empobj1)
    emp.add(empobj2)
    deptobj.setEmployee(emp)

    WriteDeptObject(deptobj)
    ReadDeptObject()

    # for emp in deptobj.getEmloyee():
    #     emp.show_emp_details()
#saving dept object in file
except ValueError :
    print("Invalid Values")

# deptobj = Department("Sales", "Mumbai") 
# addrsobj = Address("Jerbai Road", "Mumbai", "400012")
# empobj1=Manager("Mgr01",56784,2367,deptobj, addrsobj)
# empobj1.setAddress(addrsobj)
# print(empobj1.show_emp_details())
# print(empobj1.show_total_salary())





# try:
#     salary = -1000

#     if salary <= 0:
#         raise ValueError("Salary cannot be zero")

# except ValueError as e:
#     print("Value Error :", e)

# try:
#     s1 = Salesman("", 4000, 500, deptobj, addressobj)

# except Exception as e:
#     print("Exception occurred:", e)


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
