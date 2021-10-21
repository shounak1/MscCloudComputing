class Bank:
    balance = 0
    def __init__(self, money):
        self.balance = money
        
    def depositMoney(self, money):
        self.balance = self.balance + money
        
    def withdrawMoney(self, money):
        self.balance = self.balance - money
    
    def displayBalance(self):
        print ("Current Balance : ", self.balance)
        
if __name__ == "__main__":
    initial_deposit = float(input("Enter initial deposit amount : "))
    account = Bank(initial_deposit)
    while(1):
        trans_type = int(input("Transaction type \n 1. Deposit Money \n 2. Withdraw Money \n 3. Display Balance \n Input : "))
        if trans_type == 1:
            amount = float(input("Enter Amount : "))
            account.depositMoney(amount)
        elif trans_type == 2:
            amount = float(input("Enter Amount : "))
            account.withdrawMoney(amount)
        elif trans_type == 3:
            account.displayBalance()
        else:
            print ("Invalid Transaction type")
            continue
        