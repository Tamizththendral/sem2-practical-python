class Employee:
    def __init__(self,name,ID,position):
        self.name=name
        self.ID=ID
        self.position=position
    def displayemployeeinfo(self):
        print(f"name={self.name}\nID={self.ID}\nposition={self.position}")
class Address:
    def  __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayaddressinfo(self):
        print(f"street={self.street}\nstate={self.state}\ncountry={self.country}")
class Employeedetail(Employee,Address):
    def __init__(self,name,ID,position,street,state,country):
        super().__init__(name,ID,position)
        Address.__init__(self,street,state,country)
    def displayemp(self):
        self.displayemployeeinfo()
        self.displayaddressinfo()
obj= Employeedetail('Tamizh',7777,'Manager','xxx street','Tamilnadu','India')
obj.displayemp()
