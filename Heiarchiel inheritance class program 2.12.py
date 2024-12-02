class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displaystudent(self):
        print('name=',self.name,'rollno=',self.rollno)
class course(student):
    def __init__(self,name,rollno,program,department):
        super().__init__(name,rollno)
        self.program=program
        self.department=department
    def displaycourse(self):
        self.displaystudent()
        print('program=',self.program,'department=',self.department)
class detail(student):
    def __init__(self,name,rollno,ID,age):
        super().__init__(name,rollno)
        self.ID=ID
        self.age=age
    def displaydetail(self):
        print('ID=',self.ID,'age=',self.age)
cou=course('Tamizh',1232,'bsc','cs with ai')
obj=detail('Tamizh',12343 ,5678,17)
cou.displaycourse()
obj.displaydetail()
