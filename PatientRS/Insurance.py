class Insurance:
    """
    Represents an insurance policy associated with a Patient.
    Demonstrates: encapsulation (validation centralized in setters).
    """

    def __init__(self, policy_no, company, coverage):
        self.setPolicyNo(policy_no)
        self.setCompany(company)
        self.setCoverage(coverage)

    # ---------------- setters (validation happens here, nowhere else) ----------------
    def setPolicyNo(self, policy_no):
        if len(policy_no) == 0:
            raise ValueError("Policy No cannot be left blank.")
        self.policy_no = policy_no

    def setCompany(self, company):
        if len(company) == 0:
            raise ValueError("Company name cannot be left blank.")
        self.company = company

    def setCoverage(self, coverage):
        if coverage <= 0:
            raise ValueError("Coverage must be greater than zero.")
        self.coverage = coverage

    # ---------------- getters ----------------
    def getPolicyNo(self):
        return self.policy_no

    def getCompany(self):
        return self.company

    def getCoverage(self):
        return self.coverage

    # ---------------- display ----------------
    def show_insurance_details(self):
        return (f"Policy No: {self.getPolicyNo()}, "
                f"Insurance Company: {self.getCompany()}, "
                f"Coverage Amount: Rs.{self.getCoverage():,.2f}")
