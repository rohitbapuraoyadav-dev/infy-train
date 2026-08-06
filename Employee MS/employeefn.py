class Employee():
    start_empid = 1001  # Class variable

    def __init__(self,empname,salary,deptobj, address):
      self.empid = Employee.start_empid    
      Employee.start_empid +=1
      self.setEmpName(empname)
      self.setSalary(salary)
       #adding asssociation of department with Employee
       #self.department = deptobj

      self.setAddress(address)
      self.setDepartment(deptobj)

    def getDeptDetails(self):
        return self.department.showDeptDetails() #setting getter method (association of dept with employee class)

       #centralised validation logic

    def setEmpName(self,empname):
        if len(empname)==0:
           raise AttributeError("Employee name cannot be left blank")
        else :
           self.empname = empname

    def setDepartment(self, deptobj):
        self.department = deptobj

    def setAddress(self, addressobj):

        if addressobj is None:
           raise ValueError
           print("Invalid Address.")
        else:
            self.address=addressobj


    def setSalary(self,salary):
        if salary <=0 :
           raise ValueError("Salary cannot be zero")
        else :
           self.salary = salary

    def getSalary(self):
       return self.salary

    def getEmpId(self):
       return self.empid

    def getEmpName(self):
       return self.empname

    def show_emp_details(self):
        return "EmpId:",self.getEmpId(),"Employee Name:" , self.getEmpName(),"Employee salary :" , self.getSalary()

    def show_total_salary(self):
        pass


class Manager(Employee):
    def __init__(self, empname,salary,perks,deptobj,addressobj):
        super().__init__(empname, salary,deptobj,addressobj ) #pass the values to the base class
        self.setPerks(perks)

    def setPerks(self,perks):
        if perks<0 :
          raise ValueError("Perks cannot take negative value")
        else :
          self.perks = perks

    def getPerks(self):
       return self.perks



    def show_total_salary(self):
        return self.getSalary() + self.getPerks()

class Salesman(Employee):
    def __init__(self,empname,salary,commission,deptobj,addressobj):
        super().__init__(empname,salary ,deptobj,addressobj)
        self.setCommission(commission)


    def setCommission(self,commission):
       if commission<0 :
          raise ValueError("Commission cannot take negative value")
       else :
          self.commission = commission

    def getCommission(self):
       return self.commission

    def show_total_salary(self):
        return self.getSalary + self.getCommission
