class Person:
    def __init__(self,studentname):
        self.studentname=studentname
    def show_name(self):
        print(self.studentname)
class Student(Person):
    def __init__(self,studentname,studentid):
        super().__init__(studentname)
        self.studentid=studentid
    def show_studentid(self):
        print(self.studentid)
obj=Student("Tamizh",7777)
obj.show_name()
obj.show_studentid()

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print(self.name)
        print(self.salary)
class Manager(Employee):
        def __init__(self,name,salary,department):
            super().__init__(name,salary)
            self.department=department
        def display_department(self):
            print(self.department)
obj=Manager('Tamizh',7777,'AI')
obj.display_details()
obj.display_department()
