class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def displayvehicleinfo(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")
class Truck(Vehicle):
    def __init__(self, make, model, year, cargocapacity,axles):
        super().__init__(make, model, year)
        self.cargocapacity=cargocapacity
        self.axles=axles
    def displaytruckinfo(self):
        super().displayvehicleinfo()
        print(f"Cargo Capacity: {self.cargocapacity}\nAxles: {self.axles}")
class PickupTruck(Truck):
    def __init__(self, make, model, year, cargocapacity, axles, doors, trunkcapacity):
        super().__init__(make, model, year, cargocapacity,axles)
        self.doors=doors
        self.trunkcapacity=trunkcapacity
    def displaypickuptruckinfo(self):
        super().displaytruckinfo()
        print(f"Doors: {self.doors}\nTrunkCapacity: {self.trunkcapacity}")
obj=PickupTruck("mclaren", "p1", 1800, 2000, 4, 2, 500)
obj.displaypickuptruckinfo()

class Product:
    def __init__(self,Id, name, price):
        self.Id = Id
        self.name = name
        self.price = price
    def displayproductinfo(self):
        print(f"ID: {self.Id}\nName: {self.name}\nPrice: {self.price}")
class Electronics(Product):
    def __init__(self, Id, name, price, warranty, brand):
        super().__init__(Id, name, price)
        self.warranty= warranty
        self.brand = brand
    def displayproductinfo(self):
        super().displayproductinfo()
        print(f"Warranty : {self.warranty} years\nBrand: {self.brand}")
class Clothing(Product):
    def __init__(self, Id, name, price, size, material):
        super().__init__(Id, name, price)
        self.size = size
        self.material = material
    def displayproductinfo(self):
        super().displayproductinfo()
        print(f"Size: {self.size}\nMaterial: {self.material}")
obj1= Electronics(7777, "Laptop", 7777777, 2, "lenovo")
obj2= Clothing(77, "shirt", 777, "s", "Cotton")
obj1.displayproductinfo()
obj2.displayproductinfo()
