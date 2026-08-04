class Department:
    dptcount=100
    def __init__(self,deptname,loc):
        #self.setDeptName(deptname)
        self.deptname=deptname
        self.location=loc
        Department.dptcount += 1
        self.dptid=Department.dptcount

    '''def setDeptName(self,deptname):
        if(len(deptname)== 0):
            raise ValueError("Invalid name.")
        else:
            self.dptname=deptname'''

    def showDeptDetails(self):
        return "Dept ID :", self.dptid,"Dept Name :", self.deptname ,"Dept Loaction :", self.location
    