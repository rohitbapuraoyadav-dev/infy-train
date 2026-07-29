class Department:
    dptcount=100
    def __init__(self,dptname,loc):
        self.setDeptName
        #self.dptname=dptname
        self.location=loc
        Department.dptcount += 1
        self.dptid=Department.dptcount

    def setDeptName(self,deptname):
        if(len(deptname)<0):
            raise ValueError("Invalid name.")
        else:
            self.dptname=self.dptname

    def showDeptDetails(self):
        return "Dept ID :", self.dptid,"Dept Name :", self.dptname ,"Dept Loaction :", self.location
    
   