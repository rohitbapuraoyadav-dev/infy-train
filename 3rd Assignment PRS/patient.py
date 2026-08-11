class Patient:
    next_id = 1001
    def __init__(self, name, age):
        self.patient_id = Patient.next_id
        Patient.next_id += 1

        self.set_name(name)
        self.set_age(age)

        self.treatments = []
        self.insurance = None
        self.disease = None

    # Getters
    def get_patient_id(self):
        return self.patient_id
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # Setters

    def set_name(self, name):
        # this validation check first if it contains space it will replace and then check is this aplha or numeric 
        # if numeric it will raise error
        
        if not name.replace(" ", "").isalpha():  
            raise ValueError(
                "Name should contain alphabets only"
            )
        #strip :- Removes spaces from beginning and end.
        if len(name.strip()) < 3:
            raise ValueError(
                "Name should contain minimum 3 characters"
            )
        if len(name.strip()) > 40:
            raise ValueError("Name too long")
        self.name = name

    def set_age(self, age):

        if age < 0 or age > 110:
            raise ValueError( "Age must be between 0 and 110")
        self.age = age

    def add_treatment(self, treatment):
        self.treatments.append(treatment)

    def set_insurance(self, insurance):
        self.insurance = insurance

    def set_disease(self, disease):
        self.disease = disease

    def display_details(self):

        print("\nPatient Details")
        print("----------------")
        print(f"Patient ID : {self.patient_id}")
        print(f"Name       : {self.name}")
        print("Age        :", self.age)

    # keeping the method there also not effect anything but as oops way it is better to write 
    def calculate_bill(self):
        pass

# child class 
class InPatient(Patient):

    def __init__(self, name,age,room_charge,days_stayed):
        super().__init__(name, age)
        self.set_room_charge(room_charge)
        self.set_days_stayed(days_stayed)

    # Getters
    def get_room_charge(self):
        return self.room_charge

    def get_days_stayed(self):
        return self.days_stayed

    # Setters
    def set_room_charge(self, room_charge):

        if room_charge <= 0:
            raise ValueError("Room charge must be positive" )
        self.room_charge = room_charge

    def set_days_stayed(self, days_stayed):

        if days_stayed <= 0:
            raise ValueError("Days stayed must be positive")
        self.days_stayed = days_stayed

    def calculate_bill(self):

        treatment_cost = sum(treatment.get_cost() for treatment in self.treatments
        )

        return (self.room_charge *self.days_stayed) + treatment_cost

    def display_inpatient(self):

        self.display_details()
        if self.disease:
            self.disease.display_disease()

        print("\nTreatment Performed")
        print("-------------------")

        for treatment in self.treatments:
            print(f"{treatment.get_treatment_name()} "f"- ₹{treatment.get_cost()}")

        print(
            f"\nRoom Charge/Day : ₹{self.room_charge}"
        )

        print(
            f"Days Stayed     : {self.days_stayed}"
        )

        bill = self.calculate_bill()

        print(f"\nTotal Bill      : ₹{bill}")

        if self.insurance:
            covered, patient_pay = (self.insurance.calculate_coverage(bill))
            self.insurance.display_insurance()

            print(f"\nInsurance Pays : ₹{covered}")
            print(f"Patient Pays   : ₹{patient_pay}")


class OutPatient(Patient):

    def __init__(self,name,age,consultation_fee):
        super().__init__(name, age)

        self.set_consultation_fee(consultation_fee)

    # Getter

    def get_consultation_fee(self):
        return self.consultation_fee

    # Setter

    def set_consultation_fee(
            self,
            consultation_fee):

        if consultation_fee <= 0:
            raise ValueError("Consultation fee must be positive" )

        self.consultation_fee = consultation_fee

    def calculate_bill(self):

        treatment_cost = sum(treatment.get_cost()for treatment in self.treatments)

        return (self.consultation_fee + treatment_cost)
    

    def display_outpatient(self):

        self.display_details()

        if self.disease:
            self.disease.display_disease()

        print("\nTreatment Performed")
        print("-------------------")

        for treatment in self.treatments:

            print(
                f"{treatment.get_treatment_name()} "
                f"- ₹{treatment.get_cost()}"
            )

        bill = self.calculate_bill()

        print(
            f"\nConsultation Fee : ₹{self.consultation_fee}"
        )

        print(
            f"Total Bill     : ₹{bill}"
        )

        if self.insurance:
            covered, patient_pay = (
                self.insurance.calculate_coverage(bill)
            )

            self.insurance.display_insurance()

            print(f"\nInsurance Pays : ₹{covered}")
            print(f"Patient Pays   : ₹{patient_pay}")