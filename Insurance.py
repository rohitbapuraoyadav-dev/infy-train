class Insurance():
    def __init__(self,policy_no,company,coverage):
        self.setPolicyNo(policy_no)
        self.setCompany(company)
        self.setCoverage(coverage)

    def setPolicyNo(self,policy_no):
        if len(policy_no)== 0:
            raise ValueError("Policy No cannot be left blank.")
        else:
            self.policy_no=policy_no

    def setCompany(self,company):
        if len(company)==0:
            raise ValueError("Company name cannot be left blank.")
        else :
            self.company=company

    def setCoverage(self,coverage):
        if coverage<=0:
            raise ValueError("Coverage must be greater than zero.")
        else:
            self.coverage=coverage

    def show_insurance_details(self):
        return("Policy no:",self.policy_no,"Insurance Comapny :",self.company,"Coverage amount:",self.coverage)