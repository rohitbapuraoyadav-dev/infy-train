from datetime import datetime


class Treatment:
    """
    Represents a medical treatment/procedure linked to a Patient.
    Demonstrates: encapsulation, class-level (shared) data, data-driven
    business rules instead of hardcoded if/elif chains.
    """

    # ---- classification of procedures ----
    INPATIENT_PROCEDURES = [
        "Surgery", "ICU Care", "Cardiac Care",
        "Orthopedic Treatment", "Maternity Care", "Respiratory Therapy"
    ]
    OUTPATIENT_PROCEDURES = [
        "General Consultation", "Dental Treatment", "Vaccination", "Physiotherapy"
    ]
    valid_treatments = INPATIENT_PROCEDURES + OUTPATIENT_PROCEDURES

    # ---- prerequisite tests required before an in-patient procedure ----
    # (out-patient procedures do not require prerequisite tests)
    required_tests = {
        "Surgery": ["Blood Test", "ECG", "X-Ray", "Anesthesia Fitness"],
        "ICU Care": ["Blood Test", "ECG", "Chest X-Ray", "Oxygen Saturation Test"],
        "Cardiac Care": ["ECG", "Echocardiogram", "Blood Pressure Check", "Cardiac Enzyme Test"],
        "Orthopedic Treatment": ["X-Ray", "Bone Density Test", "Blood Test"],
        "Maternity Care": ["Ultrasound", "Blood Test", "Blood Pressure Check", "Urine Test"],
        "Respiratory Therapy": ["Chest X-Ray", "Pulmonary Function Test", "Oxygen Saturation Test"],
    }

    def __init__(self, doctor, treatment_type, treatment_date, cost, tests_done=None):
        self.setDoctor(doctor)
        self.setTreatmentType(treatment_type)
        self.setTestsDone(tests_done or [])
        self.checkPrerequisiteTests()             # records what's missing, does not block creation
        self.setTreatmentDate(treatment_date)
        self.setCost(cost)

    # ---------------- setters ----------------
    def setDoctor(self, doctor):
        if len(doctor) == 0:
            raise ValueError("Doctor name cannot be empty")
        self.doctor = doctor

    def setTreatmentType(self, treatment_type):
        if treatment_type not in Treatment.valid_treatments:
            raise ValueError(f"Invalid Treatment. Must be one of {Treatment.valid_treatments}")
        self.treatment_type = treatment_type

    def setTestsDone(self, tests_done):
        self.tests_done = tests_done

    def setTreatmentDate(self, treatment_date):
        t_date = datetime.strptime(treatment_date, "%Y-%m-%d").date()
        if t_date > datetime.today().date():
            raise ValueError("Treatment date cannot be in the future")
        self.treatment_date = treatment_date

    def setCost(self, cost):
        if cost <= 500:
            raise ValueError("Treatment cost must be greater than 500")
        self.cost = cost

    # ---------------- getters ----------------
    def getDoctor(self):
        return self.doctor

    def getTreatmentType(self):
        return self.treatment_type

    def getTestsDone(self):
        return self.tests_done

    def getTreatmentDate(self):
        return self.treatment_date

    def getCost(self):
        return self.cost

    # ---------------- classification helpers ----------------
    def isInpatientProcedure(self):
        return self.treatment_type in Treatment.INPATIENT_PROCEDURES

    def isOutpatientProcedure(self):
        return self.treatment_type in Treatment.OUTPATIENT_PROCEDURES

    def getRequiredTests(self):
        return Treatment.required_tests.get(self.treatment_type, [])

    def getRequiredTestCount(self):
        return len(self.getRequiredTests())

    def checkPrerequisiteTests(self):
        """
        Works out which required tests are still pending, instead of blocking
        the object from being created. Out-patient procedures have no required
        tests, so missing_tests is simply empty for them.
        """
        self.missing_tests = [t for t in self.getRequiredTests() if t not in self.tests_done]

    def getMissingTests(self):
        return self.missing_tests

    def isReadyForProcedure(self):
        return len(self.missing_tests) == 0

    # ---------------- display ----------------
    def show_treatment_details(self):
        return (f"Doctor's Name: {self.getDoctor()}, "
                f"Treatment Type: {self.getTreatmentType()}, "
                f"Treatment Date: {self.getTreatmentDate()}, "
                f"Treatment Cost: Rs.{self.getCost():,.2f}")
