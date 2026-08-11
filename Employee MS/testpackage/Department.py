
class Department:
    dptcount=100

    def __init__(self,deptname,loc):
        self.setDeptName(deptname)
            #self.deptname=deptname
        self.setDeptLoc(loc)
            #self.location=loc
        Department.dptcount += 1
        self.dptid=Department.dptcount
        print("Dept object created")
        
    def setEmployee(self,employee):
        self.Employee=employee

    def getEmployee(self):
        return self.Employee

    def setDeptName(self,deptname):
        self.deptname=deptname
        
    def setDeptLoc(self,loc):
        self.location=loc

    def getDeptName(self):
        return self.deptname
        
    def getDeptLoc(self):
        return self.location

    def getDeptId(self):
        return self.dptid        


    """
    def setDeptName(self,deptname):
        if(len(deptname)== 0):
            raise ValueError("Invalid name.")
        else:
            self.dptname=deptname'''

    def showDeptDetails(self):
        return "Dept ID :", self.dptid,"Dept Name :", self.deptname ,"Dept Loaction :", self.location
    """