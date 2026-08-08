import os
import pickle
from bankfn import Account,Savings,Current,Customer
from addrs import Address

# Account()
# try:
#     Savings("Rohit",20000,1000)  #can I have attribute error and valueerror in same 
# except ValueError :
#     print("Min Balance has to be greater than 2000")

# try:
#     Savings("",20000,2000)
# except AttributeError:
#     print("Name cannot be blank")

# try:
#     Savings.withdraw(19000)
# except ValueError:
#     print("Insufficient Balance:")

# try:
#     Current.withdraw(45000)
# except ValueError:
#     print("Overdraft limit exceeded")

try:
    addrsobj=Address("Hinjewadi","Pune","411057")
    cobj=Customer("Ganesh",addrsobj,)
    try:
        savobj=Savings(cobj,25000,2000)
        #savobj.setAddress(addrsobj)
        print(savobj.customer.address.showAddressDetails())
    
    except ValueError:
        print("Invalid Input.")

    try:
        curtobj=Current(cobj,25000,20000)
       # curtobj.setAddress(addrsobj)
        print(curtobj.show_current_acc_details(),
              cobj.showCustomerDetails())

    except ValueError:
        print("Invalid Input")

    acc=set()
    acc.add(savobj)
    acc.add(curtobj)
    cobj.setAccount(acc)

except ValueError:
    print("Invalid Values.")

# print(cobj.showCustomerDetails())
# print(addrsobj.showAddressDetails())