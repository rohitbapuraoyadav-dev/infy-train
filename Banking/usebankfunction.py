from BANKING import aCCOUNT,Savings, Current, Customer,Address

import pickle

def WriteCustomerObject(customer):
    with open("CustomerDetails.dat", "wb+") as file:
        pickle.dump(customer, file)

def ReadCustomerObject():
    with open("CustomerDetails.dat", "rb+") as file:
        custobj = pickle.load(file)

    print(custobj.showCustomerDetails())

    for account in custobj.account:

        if isinstance(account, Savings):
            print(account.show_saving_acc_details())

        elif isinstance(account, Current):
            print(account.show_current_acc_details())


try:

    addrsobj = Address("Hinjewadi", "Pune", "411057")

    cobj = Customer("Ganesh", addrsobj)

    savobj = Savings(cobj, 25000, 2000)
    print(savobj.show_bank_details())
    savobj.withdraw(2000)
    print(savobj.show_bank_details())


    curtobj = Current(cobj, 25000, 20000)
    print(curtobj.show_bank_details())
    curtobj.withdraw(2500)
    print(curtobj.show_bank_details())

    acc = set()
    acc.add(savobj)
    acc.add(curtobj)

    cobj.setAccount(acc)

    # Save object
    WriteCustomerObject(cobj)

    # Read object
    ReadCustomerObject()

except ValueError as e:
    print("Error :", e)