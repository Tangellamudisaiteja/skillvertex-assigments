import os

class Account:
    def __init__(self, acc_number, acc_holder, balance=0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of {amount} successful. Current balance: {self.balance}"
        else:
            return "Insufficient funds."

    def get_balance(self):
        return f"Current balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc_number, acc_holder, balance=0):
        new_account = Account(acc_number, acc_holder, balance)
        self.accounts.append(new_account)
        return f"Account created successfully: {acc_number}"

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def get_account(self, acc_number):
        for account in self.accounts:
            if account.acc_number == acc_number:
                return account
        return None

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for account in self.accounts:
                file.write(f"{account.acc_number},{account.acc_holder},{account.balance}\n")
        print(f"Data saved to {filename}.")

    def load_from_file(self, filename):
        acc_numbers = []
        acc_holders = []
        balances = []

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.accounts = []
                for line in lines:
                    acc_number, acc_holder, balance = line.strip().split(',')
                    acc_numbers.append(int(acc_number))
                    acc_holders.append(acc_holder)
                    balances.append(float(balance))
                    self.add_account(int(acc_number), acc_holder, int(balance))
            print(f"Data loaded from {filename}.")
        else:
            print("File not found.")

        return acc_numbers, acc_holders, balance

    def find_account(self, account_number):
        pass




# create bank account
bank = Bank()

# Add new accounts
bank.add_account(1001, "Sai Teja", 500)
bank.add_account(1002, "Sri Kanth", 1000)

# Deposit and withdraw
account1 = bank.get_account(1001)
print(account1.deposit(2000))
print(account1.withdraw(100))

# Save and load from file
bank.save_to_file('bank_data.txt')
acc_numbers, acc_holders, balances = bank.load_from_file('bank_data.txt')

# Print account details separately
for i in range(len(acc_numbers)):
    acc_number = acc_numbers[i]
    acc_holder = acc_holders[i]
    balance = balances[i]
    print(f"Account Number: {acc_number}, Account Holder: {acc_holder}, Balance: {balance}")


new_bank = Bank()
new_bank.load_from_file('bank_data.txt')


for acc_number, acc_holder, balance in zip(acc_numbers, acc_holders, balances):
    print(f"Account Number: {acc_number}, Account Holder: {acc_holder}, Balance: {balance}")



print(bank.accounts[0].deposit(100))
print(bank.accounts[1].withdraw(200))


# Print updated account details
for acc in bank.accounts:
    print(acc.get_balance())

# Save updated accounts to file
bank.save_to_file("updated_bank_data.txt")

# Create another bank instance and load accounts from the updated file
another_bank = Bank()
another_bank.load_from_file("updated_bank_data.txt")

# Print loaded account details
for acc in another_bank.accounts:
    print(acc.get_balance())







