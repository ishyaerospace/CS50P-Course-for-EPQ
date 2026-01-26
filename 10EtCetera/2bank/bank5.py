#oop version
class Account:
    def __init__(self):
        self._balance = 0 # _ indicates that the variable is private and should not be touched
        

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

    # no setter therefore account.balance = 0 wont work

if __name__ == "__main__":
    main()