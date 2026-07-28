from bankfunction import Account,Savings,Current
Account()
try:
    Savings("Rohit",20000,1000)  #can I have attribute error and valueerror in same 
except ValueError :
    print("Min Balance has to be greater than 2000")

try:
    Savings("",20000,2000)
except AttributeError:
    print("Name cannot be blank")

try:
    Savings.withdraw(19000)
except ValueError:
    print("Insufficient Balance:")

try:
    Current.withdraw(45000)
except ValueError:
    print("Overdraft limit exceeded")

