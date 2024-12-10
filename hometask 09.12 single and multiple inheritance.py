class Camera: 
    def __init__(self, resolution):
        self.resolution = resolution
    def photo(self):
        print(f"Taking a photo with resolution: {self.resolution}MP")
class Phone:
    def __init__(self, phoneno):
        self.phoneno = phoneno
    def msg(self, number, message):
        print(f"Sending message to {number}: {message}")
class Info(Camera, Phone):
    def __init__(self, brand, model, resolution, phoneno):
        Camera.__init__(self, resolution)  
        Phone.__init__(self, phoneno)  
        self.brand = brand
        self.model = model
    def displaydetails(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Camera Resolution: {self.resolution} MP")
        print(f"Phoneno: {self.phoneno}")
obj = Info("Samsung", "Galaxy Z Flip6", 50, "1234567890")
obj.displaydetails()
obj.photo()
obj.msg("0987654321", "Hi")

class Student:
    def __init__(self, name, course): 
        self.name = name
        self.course = course
    def student_info(self):
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")
class StudentAthlete(Student):
    def __init__(self, name, course, sport_name): 
        super().__init__(name, course)
        self.sport_name = sport_name
    def display_athlete_info(self):
        print("Athlete Info:")
        self.student_info()
        print(f"Sport: {self.sport_name}")
athlete = StudentAthlete("Tamizh", "AI", "Chess")
athlete.display_athlete_info()
