from prt import Patient
from prt import Inpatient,Outpatient
from Insurance import Insurance
from treatment import Treatment

try:

    insobj=Insurance("POL123","MAX Life",500000)
    treatobj=Treatment("Dr.Verma","Surgery","2026-08-02",10000)
    patientobj=Inpatient("Rohan Sharma",45,"Male","2026-07-20",insobj,4,75000)
   

    print(insobj.show_insurance_details())

    patient1= Patient("Rohan Sharma",45,"Male","2026-07-20",insobj)
    print("Insurance Available:",patient1.hasInsurance())
    print(treatobj.show_treatment_details())
    print(patientobj.show_InPatient_details())

except ValueError as e:
    print ("Error:",e)

