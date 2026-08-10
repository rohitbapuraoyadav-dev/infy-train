from testpackage import Employee

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
        return self.getSalary() + self.getCommission()
