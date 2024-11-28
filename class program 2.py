class Studentdetails:
    def __init__(self, name, rollno, mark1, mark2, mark3):
        self.name = name
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def calculate_per(self):
        total = self.mark1 + self.mark2 + self.mark3
        grade = (total / 300) * 100
        return grade
    def display_grade(self):
        grade = self.calculate_per()
        print(f"\nName: {self.name}")
        print(f"Roll Number: {self.rollno}")
        print(f"Subject 1: {self.mark1}")
        print(f"Subject 2: {self.mark2}")
        print(f"Subject 3: {self.mark3}")
        print(f"percentage: {grade}%")
    def grade(self):
        grade = self.calculate_per()
        if grade >= 90:
            print("grade: A")
        elif grade >= 80:
            print("grade: B")
        elif grade >= 70:
            print("grade: C")
        elif grade >= 50:
            print("grade: D")
        elif grade >= 40:
            print("grade: E")
        else:
            print("grade: F")
a= Studentdetails("Tamizh","1234567890",90,99,89)
a.display_grade()
a.grade()

class Studentinfo:
    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
    def display(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"course:{self.course}")
        print(f"grade:{self.grade}")
    def __del__(self):
        print("database deleted")
a = Studentinfo("Tamizh", 17, "BSc CS with AI", "B")
a.display()
del a

