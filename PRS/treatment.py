from datetime import datetime

class Treatment():
    valid_treatments = ["Surgery","Dialysis","ICU Care","Cardiac Care",
                        "Orthopedic Treatment","Maternity Care","Chemotherapy",
                        "Respiratory Therapy","Dental Treatment","Vaccination",
                        "Physiotherapy","General Consultation"]


    def __init__(self,doctor,treatment_type,treatment_date,cost):
        self.doctor=doctor
        if treatment_type not in Treatment.valid_treatments:
            raise ValueError("Invalid Treatment")
    
        self.treatment_type = treatment_type

        t_date= datetime.strptime(treatment_date,"%Y-%m-%d").date()
    
        if t_date>datetime.today().date():
            raise ValueError("Treatment date cannot be in the future")
        self.treatment_date = treatment_date

        if cost<=500:
            raise ValueError("Treatment cost must be greater than 500")
        self.cost=cost

    def show_treatment_details(self):
        return ("Doctor's name :",self.doctor,
                "Treatment type:",self.treatment_type,
                "Treatment date :",self.treatment_date,
                "Treatment Cost :",self.cost)
