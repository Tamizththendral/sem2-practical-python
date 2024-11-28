class Bankaccount:
    def __init__(self, accountholdername, accountnumber, balance):
        self.accountholdername=accountholdername
        self.accountnumber=accountnumber
        self.balance=balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} deposited. new balance: {self.balance}")
        else:
            print("Invalid amount.")
    def withdraw(self, amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f"{amount} withdrawn. remaining balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount.")
    def check_balance(self):
        print(f"Current balance: {self.balance}")
account = Bankaccount('Tamil', '56347236',214365)
account.deposit(3234)
account.withdraw(7687)
account.check_balance()


class Cosmetics:
    def __init__(self, name="lipstick", brand="maybelline", price=500, category="cosmetic"):
        self.name = name
        self.brand = brand
        self.price = price
        self.category = category

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
product = Cosmetics()  
product.display_info()
