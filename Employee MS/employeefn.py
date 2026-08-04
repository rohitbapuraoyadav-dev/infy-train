class Employee():
    start_empid = 1001  # Class variable

    def __init__(self,empname,salary,deptobj,addressobj):
      self.empid = Employee.start_empid
      Employee.start_empid +=1
      self.setEmpName(empname)
      self.setSalary(salary)
       #adding asssociation of department with Employee
       #self.department = deptobj
      self.setDepartment(deptobj)
      #setting getter method (association of dept with employee class)
      self.setAddress(addressobj)

    def getDeptDetails(self):
      return self.department.showDeptDetails()
    
    def getAddress(self):
         return self.address.showAddressDetails()

       #centralised validation logic

    def setEmpName(self,empname):
        if len(empname)==0:
           raise AttributeError("Employee name cannot be left blank")
        else :
           self.empname = empname

    def setDepartment(self, deptobj):
        self.department = deptobj

    def setAddress(self, addressobj):
        self.address=addressobj


    def setSalary(self,salary):
        if salary <=0 :
           raise ValueError("Salary cannot be zero")
        else :
           self.salary = salary

    def show_emp_details(self):
        return "Employee Name:" , self.empname,"Employee ID :" , self.empid ,"Employee salary :" , self.salary

    def show_total_salary(self):
        pass

class Manager(Employee):
    def __init__(self, empname,salary, perks, deptobj,addressobj):
        super().__init__(empname, salary,deptobj,addressobj )
        self.setPerks(perks)

    def setPerks(self,perks):
        if perks<0 :
          raise ValueError("Perks cannot take negative value")
        else :
          self.perks = perks


    def show_total_salary(self):
        return self.salary + self.perks

class Salesman(Employee):
    def __init__(self,empname,salary,commission,deptobj,addressobj):
        super().__init__(empname,salary ,deptobj,addressobj)
        self.setCommission(commission)


    def setCommission(self,commission):
       if commission<0 :
          raise ValueError("Commission cannot take negative value")
       else :
          self.commission = commission

    def show_total_salary(self):
        return self.salary + self.commission
