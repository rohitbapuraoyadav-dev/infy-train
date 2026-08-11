from datetime import datetime
from Patient import Inpatient, Outpatient
from Treatment import Treatment
from Insurance import Insurance

print("=== PRIDE Healthcare Registration System ===")

# ---- choose patient type ----
while True:
    ptype = input("Register as (I)npatient or (O)utpatient? ").strip().upper()
    if ptype in ("I", "O"):
        break
    print("Invalid input - please enter I or O.\n")

# ---- Patient Name ----
while True:
    pname = input("Patient Name: ")
    if len(pname.strip()) > 0:
        break
    print("Invalid input - name cannot be blank.\n")

# ---- DOB ----
while True:
    dob = input("DOB (YYYY-MM-DD): ")
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid input - DOB must be in YYYY-MM-DD format.\n")

# ---- Gender ----
while True:
    gender = input("Gender (Male/Female/Other): ").strip().capitalize()
    if gender in ("Male", "Female", "Other"):
        break
    print("Invalid input - gender must be Male, Female or Other.\n")

# ---- Registration Date ----
while True:
    reg_date = input("Registration Date (YYYY-MM-DD): ")
    try:
        datetime.strptime(reg_date, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid input - registration date must be in YYYY-MM-DD format.\n")

if ptype == "I":
    # ---- Treatment Type ----
    print("Available procedures:", ", ".join(Treatment.INPATIENT_PROCEDURES))
    while True:
        ttype = input("Treatment Type: ")
        if ttype in Treatment.INPATIENT_PROCEDURES:
            break
        print("Invalid input - please choose an in-patient procedure from the list above.\n")

    # ---- Completed tests ----
    required = Treatment.required_tests.get(ttype, [])
    tests_done = []
    if required:
        print("Required tests:", ", ".join(required))
        tests_done_input = input("Completed tests (comma-separated): ")
        tests_done = [t.strip() for t in tests_done_input.split(",") if t.strip()]

    # ---- Doctor's Name ----
    while True:
        doctor = input("Doctor's Name: ")
        if len(doctor.strip()) > 0:
            break
        print("Invalid input - doctor's name cannot be blank.\n")

    # ---- Treatment Date (must be on or after registration date) ----
    while True:
        treatment_date = input("Treatment Date (YYYY-MM-DD, on or after registration date): ")
        try:
            t_date = datetime.strptime(treatment_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid input - treatment date must be in YYYY-MM-DD format.\n")
            continue
        r_date = datetime.strptime(reg_date, "%Y-%m-%d").date()
        if t_date < r_date:
            print("Invalid input - treatment date must be on or after the registration date.\n")
            continue
        break

    treatment = Treatment(doctor, ttype, treatment_date, tests_done)
    print(f"Flat-rate charge for {ttype}: Rs.{treatment.getCost():,.2f}")

    # ---- Expected Stay ----
    while True:
        stay_input = input("Expected Stay (days): ")
        try:
            expected_stay = int(stay_input)
        except ValueError:
            print("Invalid input - expected stay must be a whole number.\n")
            continue
        if expected_stay <= 0:
            print("Invalid input - expected stay must be greater than zero.\n")
            continue
        break

    # ---- Insurance ----
    insurance = None
    while True:
        has_insurance = input("Do you have insurance? (Y/N): ").strip().upper()
        if has_insurance in ("Y", "N"):
            break
        print("Invalid input - please enter Y or N.\n")

    if has_insurance == "Y":
        while True:
            policy_no = input("Policy No: ")
            if len(policy_no.strip()) > 0:
                break
            print("Invalid input - policy no cannot be blank.\n")

        while True:
            company = input("Insurance Company: ")
            if len(company.strip()) > 0:
                break
            print("Invalid input - company name cannot be blank.\n")

        while True:
            coverage_input = input("Coverage Amount: ")
            try:
                coverage = float(coverage_input)
            except ValueError:
                print("Invalid input - coverage amount must be a number.\n")
                continue
            if coverage <= 0:
                print("Invalid input - coverage amount must be greater than zero.\n")
                continue
            break

        insurance = Insurance(policy_no, company, coverage)

    patient = Inpatient(pname, dob, gender, reg_date, expected_stay, treatment, insurance)

else:
    # ---- Treatment Type ----
    print("Available procedures:", ", ".join(Treatment.OUTPATIENT_PROCEDURES))
    while True:
        ttype = input("Treatment Type: ")
        if ttype in Treatment.OUTPATIENT_PROCEDURES:
            break
        print("Invalid input - please choose an out-patient procedure from the list above.\n")

    # ---- Doctor's Name ----
    while True:
        doctor = input("Doctor's Name: ")
        if len(doctor.strip()) > 0:
            break
        print("Invalid input - doctor's name cannot be blank.\n")

    # ---- Treatment Date ----
    while True:
        treatment_date = input("Treatment Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(treatment_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid input - treatment date must be in YYYY-MM-DD format.\n")

    # ---- Consultation Fee ----
    while True:
        fee_input = input("Consultation Fee: ")
        try:
            cost = float(fee_input)
        except ValueError:
            print("Invalid input - consultation fee must be a number.\n")
            continue
        if cost <= 500:
            print("Invalid input - minimum consultation fee is Rs.500.\n")
            continue
        break

    treatment = Treatment(doctor, ttype, treatment_date, cost=cost)

    # ---- Appointment Date ----
    while True:
        app_date = input("Appointment Date (YYYY-MM-DD): ")
        try:
            a_date = datetime.strptime(app_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid input - appointment date must be in YYYY-MM-DD format.\n")
            continue
        if a_date < datetime.today().date():
            print("Invalid input - appointment date cannot be in the past.\n")
            continue
        break

    # ---- Appointment Time (11:00-13:00 or 14:00-16:00) ----
    while True:
        app_time = input("Appointment Time (HH:MM): ")
        try:
            appointment = datetime.strptime(f"{app_date} {app_time}", "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid input - appointment time must be in HH:MM format.\n")
            continue

        t = appointment.time()
        morning = (datetime.strptime("11:00", "%H:%M").time()
                   <= t <= datetime.strptime("13:00", "%H:%M").time())
        afternoon = (datetime.strptime("14:00", "%H:%M").time()
                     <= t <= datetime.strptime("16:00", "%H:%M").time())
        if not (morning or afternoon):
            print("Invalid input - appointment allowed only between 11 AM-1 PM and 2 PM-4 PM.\n")
            continue
        break

    patient = Outpatient(pname, dob, gender, reg_date, treatment.getCost(), app_date, app_time, treatment)

# ---- print the registration form ----
print("\n" + "=" * 56)
print("PRIDE HEALTHCARE - PATIENT REGISTRATION FORM".center(56))
print("=" * 56)
for label, value in patient.getDetails():
    print(f"{label:<22}: {value}")
print("=" * 56)
