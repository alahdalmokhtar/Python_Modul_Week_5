class Customer:
    def __init__(self , name , surrnmae, ID_number, phone_number):
        self.name = name
        self.surrnmae = surrnmae
        self.ID_number = ID_number
        self.phone_number = phone_number

    def display_information(self):
        print(f"Name: {self.name} {self.surrnmae}")
        print(f"ID Number: {self.ID_number}")
        print(f"Phone Number: {self.phone_number}")

class Account(Customer):
    def __init__(self, name, surrnmae, ID_number, phone_number, account_number, balance):
        super().__init__(name, surrnmae, ID_number, phone_number)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def money_check(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def display_balance(self):
        print(f"Balance: {self.balance}")



Customer1 = Customer("John" , " Doe", 30, 1234)
account1 = Account("John" , " Doe", 30, 1234, 1001, 5000)
Customer1.display_information()
account1.display_balance()
account1.deposit(1000)
account1.money_check(2000)
account1.display_balance()