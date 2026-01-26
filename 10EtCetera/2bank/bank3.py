# this code will throw an UnboundLocalError

def main():# main is able to access balance
    balance = 0
    print("balance:", balance)
    deposit(100)# unable to access balance
    withdraw(50)# unable to access balance

def deposit(n):
    balance += n 

def withdraw(n):
    balance -= n 

if __name__ == "__main__":
    main()