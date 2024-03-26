class bankaccount:
    def __init__(self,accountnumber,name,balance):
        self.accountnumber=accountnumber
        self.name=name
        self.balance=balance

    def deposit(self,amount):
            if amount>0:
                self.balance+=amount
                print(f'deposit of rs{amount} is successful')
            else:
                print("invalid deposit")

    def withdraw(self,amount):
            if 0<amount<=self.balance:
                self.balance-=amount
                print(f"withdraw of Rs {amount} successful")
            else:
                print("Invalid")

    def bankfees(self):
            fees=0.05*self.balance
            self.balance-=fees
            print(f"bank fees of rs{fees} applied")

    def display(self):
            print(f"account number {self.accountnumber}")
            print(f"account holder {self.name}")
            print(f"balance {self.balance}")

account1=bankaccount(accountnumber=12345,name="john",balance=1000)
account1.display()
account1.deposit(1000)
account1.withdraw(200)
account1.bankfees()
account1.display()