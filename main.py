from Patient import Inpatient, Outpatient
from Insurance import Insurance
from Treatment import Treatment

print("=== PRIDE Healthcare Registration System ===")

try:
    ptype = input("Register as (I)npatient or (O)utpatient? ").strip().upper()

    pname = input("Patient Name: ")
    dob = input("DOB (YYYY-MM-DD): ")
    gender = input("Gender (Male/Female/Other): ")
    reg_date = input("Registration Date (YYYY-MM-DD): ")

    insurance = None
    has_ins = input("Does the patient have insurance? (y/n): ").strip().lower()
    if has_ins == "y":
        policy_no = input("Policy No: ")
        company = input("Insurance Company: ")
        coverage = float(input("Coverage Amount: "))
        insurance = Insurance(policy_no, company, coverage)

    if ptype == "I":
        print("Available procedures:", ", ".join(Treatment.INPATIENT_PROCEDURES))
        ttype = input("Treatment Type: ")

        required = Treatment.required_tests.get(ttype, [])
        tests_done = []
        if required:
            print("Required tests:", ", ".join(required))
            tests_done = [t.strip() for t in input("Completed tests (comma-separated): ").split(",") if t.strip()]

        doctor = input("Doctor's Name: ")
        treatment_date = input("Treatment Date (YYYY-MM-DD): ")
        cost = float(input("Treatment Cost: "))
        treatment = Treatment(doctor, ttype, treatment_date, cost, tests_done)

        expected_stay = int(input("Expected Stay (days): "))
        patient = Inpatient(pname, dob, gender, reg_date, insurance, expected_stay, treatment)

    else:
        print("Available procedures:", ", ".join(Treatment.OUTPATIENT_PROCEDURES))
        ttype = input("Treatment Type: ")
        doctor = input("Doctor's Name: ")
        treatment_date = input("Treatment Date (YYYY-MM-DD): ")
        cost = float(input("Treatment Cost: "))
        treatment = Treatment(doctor, ttype, treatment_date, cost)

        fee = float(input("Consultation Fee: "))
        app_date = input("Appointment Date (YYYY-MM-DD): ")
        app_time = input("Appointment Time (HH:MM): ")
        patient = Outpatient(pname, dob, gender, reg_date, fee, app_date, app_time, treatment)

    # ---- print the registration form ----
    print("\n" + "=" * 56)
    print("PRIDE HEALTHCARE - PATIENT REGISTRATION FORM".center(56))
    print("=" * 56)
    for label, value in patient.getDetails():
        print(f"{label:<22}: {value}")
    print("=" * 56)

except ValueError as e:
    print("Error:", e)
