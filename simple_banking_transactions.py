class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.new_balance = []

    def show_balance(self):
        print(f"account {self.account_number} balance : ${self.balance}")
    
    def transaction(self):
        amount = int(input(f"how much you wanna depose to your account {self.account_number} : "))
        self.balance += amount

    def show_new_balance(self):
        self.new_balance.append(self.balance)
        print(f"account {self.account_number} balance : ${self.balance}")


account_a = BankAccount("a23161500335134", 300)
account_b = BankAccount("b38759575595134", 0)
account_c = BankAccount("c29385113512423", -100)
