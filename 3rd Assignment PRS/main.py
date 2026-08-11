from Treatment import Treatment
from Insurance import Insurance
from patient import InPatient, OutPatient
from disease import Disease
import pickle

# =========================================
# Disease Data
# =========================================

appendicitis = Disease(
    "Appendicitis",
    "Inflamed/Infected Appendix",
    [
        "Physical Examination",
        "Complete Blood Count (CBC)",
        "Ultrasound Abdomen",
        "CT Scan Abdomen"
    ]
)

heart_attack = Disease(
    "Heart Attack",
    "Blocked Blood Flow to Heart",
    [
        "ECG/EKG",
        "Troponin Blood Test",
        "Echocardiogram",
        "Coronary Angiography"
    ]
)

hernia = Disease(
    "Hernia",
    "Weakness in Abdominal Wall",
    [
        "Physical Examination",
        "Ultrasound",
        "CT Scan",
        "MRI"
    ]
)

diseases = {
    1: appendicitis,
    2: heart_attack,
    3: hernia
}

# =========================================
# Treatment  Data
# =========================================

treatments = {
    1: Treatment(101, "X-Ray", 1500),
    2: Treatment(102, "Blood Test", 800),
    3: Treatment(103, "MRI Scan", 3000),
    4: Treatment(104, "CT Scan", 2500),
    5: Treatment(105, "ECG", 1000)
}

print("\n====================================")
print("     HOSPITAL MANAGEMENT SYSTEM")
print("====================================")

# =========================================
# Name Validation
# =========================================

while True:

    name = input("\n Enter Patient Name: ").strip()

    if not name.replace(" ", "").isalpha():
        print("Name should contain alphabets only.")
        continue

    if len(name) < 3:
        print("Name must contain at least 3 characters.")
        continue

    if len(name) > 40:
        print("Name cannot exceed 40 characters.")
        continue

    break

# =========================================
# Age Validation
# =========================================
while True:

    try:

        age = int(input("Enter Age: "))

        if age <= 0 or age > 120:
            print("Age must be between 1 and 120.")
            continue

        break

    except ValueError:
        print("Please enter a valid age.")
# =========================================
# Patient Type Selection
# =========================================

print("\nSelect Patient Type")
print("1. In Patient")
print("2. Out Patient")

while True:

    try:

        patient_type = int(input("Enter Choice: "))

        if patient_type not in [1, 2]:
            print("Please select 1 or 2.")
            continue

        break

    except ValueError:
        print("Enter a valid number.")

# =========================================
# Create Patient Object
# =========================================

if patient_type == 1:

    while True:
        try:

            room_charge = float(
                input("Enter Room Charge Per Day: ")
            )

            if room_charge <= 0:
                print("Room charge must be greater than 0.")
                continue

            break

        except ValueError:
            print("Enter valid room charge.")

    while True:
        try:

            days_stayed = int(
                input("Enter Days Stayed: ")
            )

            if days_stayed <= 0:
                print("Days stayed must be greater than 0.")
                continue

            if days_stayed > 365:
                print("Days stayed cannot exceed 365.")
                continue

            break

        except ValueError:
            print("Enter valid number of days.")

    patient = InPatient(name,age,room_charge,days_stayed)

else:

    while True:

        try:

            consultation_fee = float(
                input("Enter Consultation Fee: ")
            )

            if consultation_fee <= 500:
                print(
                    "Consultation fee must be greater than 500."
                )
                continue

            break

        except ValueError:
            print("Enter valid consultation fee.")

    patient = OutPatient(name,age,consultation_fee)

# =========================================
# Disease Selection
# =========================================

print("\n====================================")
print("DISEASE LIST")
print("====================================")

#this for loop iterate over the dictionary and print all the diseases list.......
for key, disease in diseases.items():
    print(f"{key}. {disease.get_disease_name()}")   # it will run getter function and take disease name 

while True:

    try:

        disease_choice = int(
            input("\nSelect Disease: ")
        )

        if disease_choice not in diseases:
            print("Invalid disease selection.")
            continue

        break

    except ValueError:
        print("Enter a valid option.")

# i have dictionary of this diseases so if i select any of the disease list eg 2 so it shows disease[2] -- means hearattack 

selected_disease = diseases[disease_choice]    # heartattack  is disease object that is stored in selected_disease variable 

patient.set_disease(selected_disease)# it goes to patient class and stored that object 

print("\nSelected Disease:")
selected_disease.display_disease()  # it will shows heartattack.displaydisease()  so python goes to disease class so in self = hearttack 

# =========================================
# Treatment Selection
# =========================================

print("\n====================================")
print("AVAILABLE TESTS / TREATMENTS")
print("====================================")

for key, treatment in treatments.items():
    print(f"{key}. "f"{treatment.get_treatment_name()} "f"- ₹{treatment.get_cost()}")

while True:

    try:

        count = int(
            input(
                "\nHow many tests were performed? "
            )
        )

        if count <= 0:
            print(
                "At least one treatment is required."
            )
            continue

        break

    except ValueError:
        print("Enter a valid number.")

# this is main line takes treatment choice from the user ---validates them and prevent duplicates means it doesnot choice same treatment again 
# add selected treatment to the patient 

# set is used to stores unique elements only
selected_tests = set()  

for i in range(count):

    while True:
        try:
            choice = int(input(f"Enter Test Number {i + 1}: "))

             # first it check the selected treatment is present in the treatment list or not 
            if choice not in treatments:
                print("Invalid test selection.")
                continue
            # it checks the selected test is already selected or only one time selected till now 
            if choice in selected_tests:
                print("This test is already selected.")
                continue

            selected_tests.add(choice) # add treatment no in set
            patient.add_treatment(treatments[choice])# add treatment to the patient class
            break
        except ValueError:
            print("Enter a valid number.")

# =========================================
# Insurance Details
# =========================================

# while true means it will goes back to top and so on till the nreak case execute it will loooping 
while True:
    insurance_choice = input("\nDoes Patient Have Insurance? (Y/N): ").upper()

    if insurance_choice in ["Y", "N"]:
        break
    print("Please enter Y or N.")

if insurance_choice == "Y":

    while True:

        policy_no = input("Enter Policy Number: ").strip()

        if len(policy_no) < 5:
            print("Policy number must contain ""at least 5 characters.")

        else:
            break

    while True:

        provider = input("Enter Provider Name: ").strip()

        if not provider.replace(" ", "").isalpha():
            print(
                "Provider name should "
                "contain alphabets only."
            )

        else:
            break

    while True:

        try:

            coverage_amount = float(
                input("Enter Coverage Amount: ")
            )

            if coverage_amount <= 0:
                print(
                    "Coverage amount must "
                    "be greater than 0."
                )
                continue

            break

        except ValueError:
            print(
                "Enter valid coverage amount."
            )

    insurance = Insurance(policy_no,provider,coverage_amount)
    patient.set_insurance(insurance)

# =========================================
# Final Hospital Report
# =========================================

print("\n")
print("=======================================")
print("  FINAL HOSPITAL REPORT   ")
print("=======================================")


# =========================================
# SERIALIZATION :- # Converting an object into bytes and storing it in a file.
# =========================================
with open("patient.dat", "wb") as file:
    pickle.dump(patient, file) # pass the patient object
print("\nPatient Object Saved Successfully.")

# =========================================
# DESERIALIZATION:- Reading the object back from the file.
# =========================================

with open("patient.dat", "rb") as file:
    loaded_patient = pickle.load(file)# load the object back into the file 
print("Patient Object Loaded Successfully.")

# =========================================
# DISPLAY LOADED OBJECT

print("\n=======================================")

# isinstance() is a built-in Python function used to check whether an object belongs to a particular class.
# syntax: isinstance(object, class_name)

if isinstance(loaded_patient, InPatient): # as of now we stored inpatient object thats why we add inpatient class name 
    loaded_patient.display_inpatient()
else:
    loaded_patient.display_outpatient()

print("\n=======================================")
print(" THANK YOU")
