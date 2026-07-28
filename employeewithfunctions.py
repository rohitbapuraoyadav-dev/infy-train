class Employee():
    start_empid = 1001  # Class variable

    def __init__(self,empname,salary):
       self.empid = Employee.start_empid
       Employee.start_empid +=1
       self.setEmpName(empname)
       self.setSalary(salary)

       #centralised validation logic

    def setEmpName(self,empname):
        if len(empname)<0:
           raise AttributeError("Employee name cannot be left blank")
        else :
           self.empname = empname

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
    def __init__(self, empname,salary, perks):
        super().__init__(empname, salary)
        self.setPerks(perks)

    def setPerks(self,perks):
       if perks<=0 :
          raise ValueError("Perks cannot take negative value")
       else :
          self.perks = perks


    def show_total_salary(self):
        return self.salary + self.perks

class Salesman(Employee):
    def __init__(self,empname,salary,commission):
        super().__init__(empname,salary)
        self.setCommission(commission)


    def setCommission(self,commission):
       if commission<=0 :
          raise ValueError("Commission cannot take negative value")
       else :
          self.commission = commission

    def show_total_salary(self):
        return self.salary + self.commission

M1= Manager("Jhon",125000,50000)
print(M1.show_total_salary())
M1.show_emp_details()

S1= Salesman("Ron",100000,10000)
print(S1.show_total_salary())
S1.show_emp_details()






