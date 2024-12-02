class Library():
    def __init__(self,bookname,author,price):
        self.bookname=bookname
        self.author=author
        self.price=price
    def displaylib(self):
        print(f'bookname={self.bookname}\nauthor={self.author}\nbookprice={self.price}')
class Member():
    def __init__(self,name,ID,number):
        self.name=name
        self.ID=ID
        self.number=number
    def displaymem(self):
        print(f'name={self.name}\nID={self.ID}\nnumber={self.number}')
class Librarymanagement(Library,Member):
    def __init__(self,bookname,author,price,name,ID,number):
        super().__init__(bookname,author,price)
        Member.__init__(self,name,ID,number)
    def displayinfo(self):
        self.displaylib()
        self.displaymem()
obj=Librarymanagement('Harry potter','J.K.Rowling',7777,'Tamizh',1234,1234567890)
obj.displayinfo()

class Restaurant:
    def __init__(self):
        self.menu = {
            "Pizza": 8.99,
            "Momo": 5.49,
            "Noodles": 6.99,
            "Burger": 5.99
        }
    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")
    def prepare_food(self, food_item):
        if food_item in self.menu:
            print(f"Preparing {food_item}...")
        else:
            print(f"Sorry, {food_item} is not on the menu.")

class Delivery:
    def __init__(self):
        self.delivery_riders = {
            "Rider1": "Available",
            "Rider2": "Available",
            "Rider3": "Unavailable"
        }
    def assign_rider(self):
        for rider, status in self.delivery_riders.items():
            if status == "Available":
                print(f"Assigning {rider} for delivery...")
                self.delivery_riders[rider] = "Unavailable"
                return rider
        return "No riders available"
    def deliver_food(self, rider, delivery_address):
        print(f"{rider} devilering the food to {delivery_address}.")
class Order(Restaurant, Delivery):
    def __init__(self, food_item, delivery_address):
        Restaurant.__init__(self)
        Delivery.__init__(self)
        self.food_item = food_item
        self.delivery_address = delivery_address
    def process_order(self):
        if self.food_item in self.menu:
            self.prepare_food(self.food_item)
            rider = self.assign_rider()
            if rider != "No riders available":
                self.deliver_food(rider, self.delivery_address)
            else:
                print(rider)
        else:
            print(f"Sorry, {self.food_item} is not available.")
obj = Order("Pizza", "chennai")
obj.process_order()
