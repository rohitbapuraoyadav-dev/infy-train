from datetime import datetime


class Patient:
    """
    Base class for all patient types.
    Demonstrates: encapsulation (validated setters/getters), class variable
    (shared ID counter), association (Patient "has-a" Insurance), and the
    polymorphic getDetails() contract every subclass extends.
    """

    patient_id = 1000  # class variable - shared counter across ALL Patient instances
                        # (including Inpatient/Outpatient, since they don't redefine it)

    def __init__(self, pname, dob, gender, reg_date, insurance=None):
        self.setPname(pname)
        self.setDob(dob)
        self.setGender(gender)
        self.setRegDate(reg_date)
        self.setInsurance(insurance)           # association with Insurance class
        Patient.patient_id += 1
        self.p_id = Patient.patient_id

    # ---------------- setters ----------------
    def setPname(self, pname):
        if len(pname) <= 0:
            raise ValueError("Patient name cannot be empty")
        self.pname = pname

    def setDob(self, dob):
        try:
            datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            raise ValueError("DOB must be in YYYY-MM-DD format")
        self.dob = dob

    def setGender(self, gender):
        if gender not in ("Male", "Female", "Other"):
            raise ValueError("Gender must be Male, Female or Other")
        self.gender = gender

    def setRegDate(self, reg_date):
        try:
            datetime.strptime(reg_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Registration date must be in YYYY-MM-DD format")
        self.reg_date = reg_date

    def setInsurance(self, insurance):
        self.insurance = insurance             # None allowed - not every patient is insured

    # ---------------- getters ----------------
    def getPID(self):
        return self.p_id

    def getPname(self):
        return self.pname

    def getDob(self):
        return self.dob

    def getGender(self):
        return self.gender

    def getRegDate(self):
        return self.reg_date

    def getInsurance(self):
        return self.insurance

    # ---------------- computed / derived ----------------
    def getAge(self):
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d").date()
        today = datetime.today().date()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def hasInsurance(self):
        return self.insurance is not None

    def getInsuranceDetails(self):
        if self.hasInsurance():
            return self.insurance.show_insurance_details()
        return "No insurance on record"

    # ---------------- polymorphic details for the registration form ----------------
    def getDetails(self):
        """
        Returns the identity fields common to every patient type as a list
        of (label, value) tuples. Inpatient/Outpatient call super().getDetails()
        and append their own fields - the printer never needs to know which
        subclass it's dealing with (polymorphism instead of isinstance checks).
        """
        fields = [
            ("Patient ID", self.getPID()),
            ("Name", self.getPname()),
            ("DOB", self.getDob()),
            ("Age", self.getAge()),
            ("Gender", self.getGender()),
            ("Registration Date", self.getRegDate()),
            ("Insurance", "Yes" if self.hasInsurance() else "No"),
        ]
        if self.hasInsurance():
            ins = self.getInsurance()
            fields += [
                ("Policy No", ins.getPolicyNo()),
                ("Insurance Company", ins.getCompany()),
                ("Coverage", f"Rs.{ins.getCoverage():,.2f}"),
            ]
        return fields

    def show_patient_details(self):
        return (f"Patient ID: {self.getPID()}, Patient Name: {self.getPname()}, "
                f"Age: {self.getAge()}, Gender: {self.getGender()}, "
                f"Registration Date: {self.getRegDate()}")


class Inpatient(Patient):
    """
    Derived class for admitted patients.
    Demonstrates: inheritance, method overriding, and a system-generated
    ESTIMATE (not a final bill - that belongs to a downstream billing module
    that runs after discharge, outside this registration system's scope).
    """

    # illustrative flat-rate base costs per procedure
    procedure_base_cost = {
        "Surgery": 60000,
        "ICU Care": 15000,
        "Cardiac Care": 80000,
        "Orthopedic Treatment": 45000,
        "Maternity Care": 35000,
        "Respiratory Therapy": 20000,
    }
    daily_room_charge = 2000

    def __init__(self, pname, dob, gender, reg_date, insurance, expected_stay_days, treatment):
        super().__init__(pname, dob, gender, reg_date, insurance)
        self.setExpectedStayDays(expected_stay_days)
        self.setTreatment(treatment)
        self.setEstimatedBill(self.calculateEstimatedBill())

    # ---------------- setters ----------------
    def setExpectedStayDays(self, days):
        if days <= 0:
            raise ValueError("Expected stay must be at least 1 day")
        self.expected_stay_days = days

    def setTreatment(self, treatment):
        if not treatment.isInpatientProcedure():
            raise ValueError(f"{treatment.getTreatmentType()} is not a valid in-patient procedure")
        self.treatment = treatment

    def setEstimatedBill(self, amount):
        if amount < 0:
            raise ValueError("Estimated bill cannot be negative")
        self.estimated_bill = amount

    # ---------------- getters ----------------
    def getExpectedStayDays(self):
        return self.expected_stay_days

    def getTreatment(self):
        return self.treatment

    def getEstimatedBill(self):
        return self.estimated_bill

    # ---------------- computed ----------------
    def calculateEstimatedBill(self):
        base = Inpatient.procedure_base_cost.get(self.treatment.getTreatmentType(), 0)
        room_charges = Inpatient.daily_room_charge * self.getExpectedStayDays()
        return base + room_charges

    def getEstimatedPayable(self):
        """Estimate only, for pre-authorization purposes - not a final invoice."""
        if not self.hasInsurance():
            return self.getEstimatedBill()
        payable = self.getEstimatedBill() - self.getInsurance().getCoverage()
        return max(payable, 0)

    # ---------------- overridden polymorphic details ----------------
    def getDetails(self):
        fields = super().getDetails()          # base identity fields first
        treatment = self.treatment
        if treatment.isReadyForProcedure():
            tests_status = f"All {treatment.getRequiredTestCount()} prerequisite tests completed"
        else:
            tests_status = (f"{len(treatment.getTestsDone())}/{treatment.getRequiredTestCount()} completed, "
                             f"pending: {', '.join(treatment.getMissingTests())}")
        fields += [
            ("Procedure", self.treatment.getTreatmentType()),
            ("Prerequisite Tests", tests_status),
            ("Expected Stay", f"{self.getExpectedStayDays()} day(s)"),
            ("Estimated Bill", f"Rs.{self.getEstimatedBill():,.2f}"),
            ("Estimated Payable", f"Rs.{self.getEstimatedPayable():,.2f}"),
        ]
        return fields

    def show_InPatient_details(self):
        return " | ".join(f"{label}: {value}" for label, value in self.getDetails())


class Outpatient(Patient):
    """
    Derived class for walk-in / scheduled-appointment patients.
    Demonstrates: inheritance, method overriding, and a different set of
    validation rules (appointment slot windows) that don't apply to Inpatient.
    """

    def __init__(self, pname, dob, gender, reg_date, consult_fee, app_date, app_time, treatment):
        super().__init__(pname, dob, gender, reg_date)
        self.setTreatment(treatment)
        self.setConsultationFee(consult_fee)
        self.setAppointmentTime(app_date, app_time)

    # ---------------- setters ----------------
    def setTreatment(self, treatment):
        if not treatment.isOutpatientProcedure():
            raise ValueError(f"{treatment.getTreatmentType()} is not a valid out-patient procedure")
        self.treatment = treatment

    def setConsultationFee(self, amount):
        if amount <= 500:
            raise ValueError("Minimum Consultation Fee is Rs.500.")
        self.consult_fee = amount

    def setAppointmentTime(self, app_date, app_time):
        appointment = datetime.strptime(f"{app_date} {app_time}", "%Y-%m-%d %H:%M")

        if appointment.date() < datetime.today().date():
            raise ValueError("Appointment date cannot be in the past")

        t = appointment.time()
        morning = (datetime.strptime("11:00", "%H:%M").time()
                   <= t <= datetime.strptime("13:00", "%H:%M").time())
        afternoon = (datetime.strptime("14:00", "%H:%M").time()
                     <= t <= datetime.strptime("16:00", "%H:%M").time())

        if not (morning or afternoon):
            raise ValueError("Appointment allowed only between 11 AM-1 PM and 2 PM-4 PM.")
        self.appointment = appointment

    # ---------------- getters ----------------
    def getTreatment(self):
        return self.treatment

    def getConsultationFee(self):
        return self.consult_fee

    def getAppointmentTime(self):
        return self.appointment

    # ---------------- overridden polymorphic details ----------------
    def getDetails(self):
        fields = super().getDetails()
        fields += [
            ("Procedure", self.treatment.getTreatmentType()),
            ("Consultation Fee", f"Rs.{self.getConsultationFee():,.2f}"),
            ("Appointment", str(self.getAppointmentTime())),
        ]
        return fields

    def show_Outpatient_details(self):
        return " | ".join(f"{label}: {value}" for label, value in self.getDetails())
