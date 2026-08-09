from datetime import datetime

class Patient():
    patient_id = 1001 #class variable,initiate patient id.
    def __init__(self,pname,dob,gender,reg_date,insurance=None):
        self.pname=pname
        self.dob = dob
        self.gender = gender
        self.reg_date = reg_date
        self.insurance=insurance # associated class
        self.p_id = Patient.patient_id #only after validation of other data members the patient id is generated
        Patient.patient_id +=1

    def getAge(self):
        birth_date=datetime.strptime(self.dob,"%Y-%m-%d").date()
        today = datetime.today().date()

        age=today.year - birth_date.year

        if (today.month,today.day)<(birth_date):
            age-= 1
        return age

    

    def hasInsurance(self):
        return self.insurance is not None

    def show_patient_details(self):
        return("Patient ID :",self.p_id,"Patient Name :",
               self.pname,"Age :",self.age,"Gender :",self.gender,
               "Registration Date:",self.reg_date)

    #inpatient and outpatient as derived classes  
from datetime import datetime

class Outpatient(Patient):
    def __init__(self, pname, age, gender, reg_date, consult_fee, app_time):
        super().__init__(pname, age, gender, reg_date)

        self.setConsultationfee(consult_fee)
        self.setAppointmentTime(app_time)

    def setConsultationfee(self, amount):
        if amount <= 500:
            raise ValueError("Minimum Consultation Fee is Rs.500.")
        else:
            self.consult_fee = amount

    def setAppointmentTime(self, app_date,app_time):

        appointment = datetime.strptime(
            f"{app_date} {app_time}",
            "%Y-%m-%d %H:%M")
        
        if appointment.date()<datetime.today().date():
            raise ValueError("Appointment date cannot be in the past")
        app_time = appointment.time()

        if (
            datetime.strptime("11:00", "%H:%M").time()
            <= app_time
            <= datetime.strptime("13:00", "%H:%M").time()
            ) or (
            datetime.strptime("14:00", "%H:%M").time()
            <= app_time
            <= datetime.strptime("16:00", "%H:%M").time()):
            self.appointment = appointment
            self.app_time=app_time
        else:
            raise ValueError("Appointment allowed only between 11 AM-1 PM and 2 PM-4 PM.")

    def show_Outpatient_details(self):
        return f"""
        "Patient ID: {self.p_id}"
        "Patient Name: {self.pname}"
        "DOB:{self.dob}"
        "Age: {self.getAge()} "
        "Gender: {self.gender} "
        "Registration Date: {self.reg_date} "
        "Consultation Fee: {self.consult_fee} "
        "Appointment Time: {self.app_time}" """

class Inpatient(Patient):
    def __init__(self, pname, dob, gender, reg_date,insurance,days_admitted,total_bill):
            super().__init__(pname, dob, gender, reg_date,insurance)

            self.setDaysAdmitted(days_admitted)
            self.setTotalBill(total_bill)

    def setDaysAdmitted(self,days_admitted):
        if days_admitted<=0:
            raise ValueError("Inpatient must be admitted for atleast 1 day.")
        else :
            self.days_admitted = days_admitted

    def setTotalBill(self,total_bill):
        if total_bill<0:
            raise ValueError("Total Bill cannot be negative")
        else :
            self.total_bill = total_bill

    def getFinalBill(self):

        final_bill=(self.total_bill-self.insurance.coverage)
        return max(final_bill,0)

    def show_InPatient_details(self):
        return f"""
                "Patient ID: {self.p_id} "
                "Patient Name: {self.pname} "
                "DOB:":{self.dob}"
                "Age: {self.getAge()} "
                "Gender: {self.gender} "
                "Registration Date: {self.reg_date}"
                "Total day admitted: {self.days_admitted} "
                "Total Bill : {self.total_bill}"
                "Insurance Coverage : {self.insurance.coverage}"
                "Final Payable Bill : {self.getFinalBill()}" """
    