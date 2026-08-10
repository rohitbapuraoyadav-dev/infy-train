from testpackage import Employee

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
        return self.getSalary() + self.getCommission()
