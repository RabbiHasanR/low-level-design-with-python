class BankAccount:
    
    def __init__(self, account_number, balance) -> None:
        self.__account_number = account_number
        self.__balance = balance
    
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid amount: Deposite failed.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw: &{amount}")
        else:
            print(f"Invalid amount or insufficient balance")
    
    def get_blance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number


# Usage
account = BankAccount("123456789", 1000)
account.deposite(500)
account.withdraw(200)
print(account.get_blance())
print(account.get_account_number())
print(account.__balance)
print(account.__account_number)
