class Disease:
    def __init__(self,disease_name,admission_reason,tests):
        self.set_disease_name(disease_name)
        self.set_admission_reason(admission_reason)
        self.set_tests(tests)
        
    # Getters
    def get_disease_name(self):
        return self.disease_name

    def get_admission_reason(self):
        return self.admission_reason

    def get_tests(self):
        return self.tests

    # =====================
    # Setters Method:- 

    def set_disease_name(self, disease_name):
        if not disease_name.strip():    # strip will remove the empty space from left and right side 
            raise ValueError("Disease name cannot be empty")
        self.disease_name = disease_name

    def set_admission_reason(self,admission_reason):
        if not admission_reason.strip():
            raise ValueError("Admission reason cannot be empty")
        self.admission_reason = admission_reason

    def set_tests(self, tests):
        if len(tests) == 0:
            raise ValueError(
                "At least one test is required"
            )

        self.tests = tests

    def display_disease(self):

        print("\nDisease Details")
        print("----------------")
        print(f"Disease Name : {self.disease_name}")
        print(f"Reason : {self.admission_reason}")
        print("\nRecommended Diagnostic Tests:")
        for test in self.tests:
            print(f"- {test}")