class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print('name=',self.name,'age=',self.age)
class Employee(Person):
    def __init__(self,name,age,ID):
        super().__init__(name,age)
        self.ID=ID
    def displayEmployee(self):
        self.displayPerson()
        print('ID=',self.ID)
class Manager(Employee):
    def __init__(self,name,age,ID,salary):
        super().__init__(name,age,ID)
        self.salary=salary
    def displayManager(self):
        self.displayEmployee()
        print('salary=',self.salary)
emp=Manager('Diana',35,100,20000)
emp.displayManager()
