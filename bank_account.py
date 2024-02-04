import random

class BankAccount:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(1000, 9999)
        self.transaction_history = []
        self.loan_limit = 2
        self.loan_taken = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited Rs{amount}")
            return f"Rs{amount} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew Rs{amount}")
            return f"Rs{amount} withdrawn successfully."
        else:
            return "Withdrawal amount exceeded."

    def check_balance(self):
        return f"Available balance: Rs{self.balance}"

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_limit > 0:
            self.balance += amount
            self.loan_taken += amount
            self.loan_limit -= 1
            self.transaction_history.append(f"Loan taken: Rs{amount}")
            return f"Loan of Rs{amount} taken successfully."
        else:
            return "You have reached the maximum loan limit."

    def transfer(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.transaction_history.append(f"Transferred Rs{amount} to account {target_account.account_number}")
            return f"Rs{amount} transferred to account {target_account.account_number} successfully."
        else:
            return "Insufficient balance for the transfer."