class Insurance:

    def __init__(self, policy_no, provider, coverage_amount):
        self.set_policy_no(policy_no)
        self.set_provider(provider)
        self.set_coverage_amount(coverage_amount)

    # getter method 
    def get_policy_no(self):
        return self.policy_no

    def get_provider(self):
        return self.provider

    def get_coverage_amount(self):
        return self.coverage_amount
    
    # Setter method
    def set_policy_no(self, policy_no):
        if not policy_no.strip():
            raise ValueError("Policy Number cannot be empty")

        if len(policy_no) < 5:
            raise ValueError(
                "Policy Number must contain minimum 5 characters"
            )

        self.policy_no = policy_no

    def set_provider(self, provider):

        if not provider.replace(" ", "").isalpha():
            raise ValueError("Provider name should contain only alphabets")
        self.provider = provider

    # Validation for coverage amount
    def set_coverage_amount(self, coverage_amount):
        if coverage_amount <= 0:
            raise ValueError(
                "Coverage amount must be greater than 0"
            )
        self.coverage_amount = coverage_amount

    def calculate_coverage(self, bill):
        covered_amount = min(bill,self.coverage_amount)
        patient_pay = bill - covered_amount
        return covered_amount, patient_pay

    def display_insurance(self):

        print("\nInsurance Details")
        print("------------------")
        print(
            f"Policy No      : {self.policy_no}"
        )
        print(
            f"Provider       : {self.provider}"
        )
        print(
            f"Coverage Limit : ₹{self.coverage_amount}"
        )