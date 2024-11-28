class Inventory:
    def getInventoryInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
        self.count=int(input("Enter the Count:"))
    def displayInventoryInfo(self):
        print("ID = ",self.id,"\nName = ",self.name,"\nCount = ",self.count)

class Perks(Inventory):
    def getDetails(self):
        self.getInventoryInfo()
        self.price=int(input("Enter the price: "))
    def displayInfo(self):
        self.displayInventoryInfo()
        print("Price = ",self.price)

p=Perks()
p.getDetails()
p.displayInfo()

class Inventory:
    def __init__(self, prodID, prodName, prodCount):  
        self.prodID = prodID
        self.prodName = prodName
        self.prodCount = prodCount
    def display(self):
        print(f"Product ID = {self.prodID}")
        print(f"Product Name = {self.prodName}")
        print(f"Product Count = {self.prodCount}")
prod = Inventory(5678,'book',7777)
prod.display() 
