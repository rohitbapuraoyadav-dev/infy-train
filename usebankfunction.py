from bankfn import Account,Customer,Savings
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
    addrsobj=Address("Hinjewadi","Pune","322123")
    cobj=Customer("Ganesh",addrsobj,)
    savobj=Savings(cobj,25000,2000)
    print(savobj.show_saving_acc_details(),cobj.showCustomerDetails())
    savobj.Deposit(5000)
except ValueError:
    print("Invalid Input.")

print(cobj.showCustomerDetails())
print(addrsobj.showAddressDetails())