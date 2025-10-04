class BankAccount:
    def __init__(self, __balance):
        self.__balance = __balance

    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
#print(account.__balance)  # Output: 1000
print(account.get_balance())  # Output: 1000
print(account._BankAccount__balance)  # name mangling // truy xuất biến private

class SavingsAccount(BankAccount):
    def __init__(self, __balance, __interest_rate):
        super().__init__(__balance)
        self.__interest_rate = __interest_rate

    def add_interest(self):
        self._BankAccount__balance += self._BankAccount__balance * self.__interest_rate
        return self._BankAccount__balance