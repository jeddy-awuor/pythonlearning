#It restricts access to certain attributes and methods to prevent direct modification

class BankAcc:
    def __init__(self,balance):
        self.__balance= balance
    def deposit(self,amount):
        if amount > 0:
           self.__balance += amount
            
    def getbalance(self):
        return self.__balance

account=BankAcc(17000)
account.deposit(4000)
print("Balance", account.getbalance())