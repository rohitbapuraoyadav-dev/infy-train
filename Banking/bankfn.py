class Account():
    account_no = 100001 # initiate account no
    def __init__(self, customer, bal):
        self.setCustomer(customer)
        self.setBal(bal)
        self.acc_no=Account.account_no
        Account.account_no += 1

    def setCustomer(self,customer):
        self.customer=customer

    def setBal(self,amount):
        if amount<0:
            raise ValueError("You cannot withdraw")
        else:
            self.bal=amount

    def deposit(self,amount):
        if amount<0:
            raise ValueError("Enter valid input")
        else:
            self.bal+=amount

    def withdraw(self, amount):
        pass

    def show_bank_details(self):
        return ("Account No :", self.acc_no,
                "Account Holder Details:",self.customer.showCustomerDetails(self),
                "Balance:",self.bal)#"IFSC Code :", self.IFSC_Code cannot be because we are writing code for individual bank account




# saving acc under the parent class Bank

class Savings(Account):
    def __init__(self,customer, bal, minbal):
        super().__init__(customer,bal)
        #self.minbal = minbal
        self.setMinBal(minbal)

#check min bal
    def setMinBal(self,amount):
        if amount<=0:
           raise ValueError("Deposit has to be positive")
        else:
            self.minbal = amount
            

    def withdraw(self,amount):
    #check withdraw condition
        if amount > (self.bal - self.minbal):
            raise ValueError("Insufficient Balance")
            #print("You can withdraw,mention the amount :")
        else:
            self.bal -= amount

        def show_saving_acc_details(self):
            return (
        "Account No:", self.acc_no,
        "Balance:", self.bal,
        "Minimum Balance:", self.minbal)

   
class Current(Account):
    def __init__(self,customer,bal ,overdraft): 
        super().__init__(customer, bal)
        #self.overdraft = overdraft
        self.setOverdraft(overdraft)

    def setOverdraft(self,amount):
        if amount<=0:
            raise ValueError("Invalid amount")
        else:
            self.overdraft = amount

    def withdraw(self, amount):
        #allowed max limit
        max_allowed=self.bal + self.overdraft
        if amount > max_allowed:
            raise ValueError("Overdraft limit exceeded:")
        else:
            self.bal -= amount
    
    def show_current_acc_details(self):
        return f"""
        Account No:{self.acc_no}
        Balance:{self.bal}
        Overdraft:{self.overdraft}"""

class Customer:
    CustID=100
    def __init__(self,customername,address):
        self.customername=customername
        self.address=address
        Customer.CustID +=1
        self.customerid= Customer.CustID

    def setAccount(self,account):
        self.account=account

    def showCustomerDetails(self):
        return f"""
        Customer ID :{self.customerid}
        Customer Name :{self.customername}
        Customer Address :{self.address.showAddressDetails()}"""



# sobj=Savings("Rohit",20000,2000)
# print(sobj.show_saving_acc_details())
# sobj.withdraw(1000)                     #Previously :In your Savings class, I defined withdraw with a lowercase(withdraw) but calling with a upppercase(Withdraw)
# print(sobj.show_saving_acc_details())
# sobj.deposit(10000)
# print(sobj.show_saving_acc_details())

# cobj=Current("Rohit",20000,20000)
# print(cobj.show_current_acc_details())
# cobj.withdraw(25000)                     
# print(cobj.show_current_acc_details())
# cobj.deposit(10000)

