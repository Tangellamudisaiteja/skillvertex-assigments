import os
import json

class Account:
    def __init__(self, acc_number, holder_name, balance=0.0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} into account {self.acc_number}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount} from account {self.acc_number}. New balance: {self.balance}"
        else:
            return f"Insufficient funds in account {self.acc_number}. Balance: {self.balance}"

    def get_balance(self):
        return f"Balance of account {self.acc_number}: {self.balance}"

    def to_dict(self):
        return {
            "acc_number": self.acc_number,
            "holder_name": self.holder_name,
            "balance": self.balance
        }

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, acc_number, holder_name, balance=0.0):
        account = Account(acc_number, holder_name, balance)
        self.accounts.append(account)
        return f"Account {acc_number} added to {self.name} bank."

    def get_account(self, acc_number):
        for account in self.accounts:
            if account.acc_number == acc_number:
                return account
        return None

    def save_to_file(self, filename):
        data = {"accounts": [account.to_dict() for account in self.accounts]}
        with open(filename, 'w') as file:
            json.dump(data, file)
        return f"Bank data saved to {filename}."

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.accounts = [Account(acc['acc_number'], acc['holder_name'], acc['balance']) for acc in data['accounts']]
            return f"Bank data loaded from {filename}."
        else:
            return f"{filename} does not exist. No data loaded."
def main():
    bank = Bank("MyBank")

    while True:
        print("\n1. Add account\n2. Deposit\n3. Withdraw\n4. Check Balance\n9. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            acc_number = int(input("Enter account number: "))
            holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance (default is 0.0): "))
            print(bank.add_account(acc_number, holder_name, initial_balance))

        elif choice == '2':
            acc_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(acc_number)
            if account:
                print(account.deposit(amount))
            else:
                print(f"Account {acc_number} not found.")

        elif choice == '3':
            acc_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(acc_number)
            if account:
                print(account.withdraw(amount))
            else:
                print(f"Account {acc_number} not found.")

        elif choice == '4':
            acc_number = int(input("Enter account number: "))
            account = bank.get_account(acc_number)
            if account:
                print(account.get_balance())
            else:
                print(f"Account {acc_number} not found.")

        elif choice == '9':
            filename = input("Enter filename to save bank data: ")
            print(bank.save_to_file(filename))
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()