class Account():
    account_no = 100001 # initiate account no
    def __init__(self, acc_hol, bal):
        self.acc_hol= acc_hol
        self.bal = bal
        self.acc_no=Account.account_no
        Account.account_no += 1

    def show_bank_details(self):
        return ("Account No :", self.acc_no,"Name :",self.acc_hol ,"Balance :",self.bal ,"IFSC Code :", self.IFSC_Code)

    def Deposit(self, amount):
        self.bal += amount

    def Withdraw(self, amount):
        pass

# saving acc under the parent class Bank

class Savings(Account):
    def __init__(self,acc_hol, bal, minbal):
        super().__init__(acc_hol,bal)
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
        return("Account No :", self.acc_no,"Name :",self.acc_hol ,"Balance :",self.bal, "Min Bal:", self.minbal)

   
class Current(Account):
    def __init__(self,acc_hol,bal ,overdraft): 
        super().__init__(acc_hol, bal)
        #self.overdraft = overdraft
        self.setOverdraft(overdraft)

    def setOverdraft(self,amount):
        if amount<=0:
            raise ValueError("Invalid amount")
        else:
            self.overdaft = amount

    def withdraw(self, amount):
        
        #allowed max limit
        max_allowed=self.bal + self.overdraft
        if amount > max_allowed:
            raise ValueError("Overdraft limit exceeded:")
        else:
            self.bal -= amount

    def show_current_acc_details(self):
        return ("Account No :", self.acc_no,"Name :",self.acc_hol ,"Balance :",self.bal, " Over draft ", self.overdaft)


sobj=Savings("Rohit",20000,2000)
print(sobj.show_saving_acc_details())
sobj.withdraw(1000)                     #Previously :In your Savings class, I defined withdraw with a lowercase(withdraw) but calling with a upppercase(Withdraw)
print(sobj.show_saving_acc_details())
sobj.Deposit(10000)
print(sobj.show_saving_acc_details())