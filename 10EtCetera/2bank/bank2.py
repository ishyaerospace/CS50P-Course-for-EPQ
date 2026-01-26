# this code will throw an UnboundLocalError

balance = 0

def main():# needs to access balance
    print("balance:", balance) # able to print the global variable
    deposit(100)
    withdraw(50)

def deposit(n): # needs to access balance
    balance += n #unable to write to a global variable

def withdraw(n): # needs to access balance
    balance -= n #unable to write to a global variable

if __name__ == "__main__":
    main()