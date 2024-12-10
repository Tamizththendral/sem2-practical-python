class Series:
    def __init__(self, name,year):
        self.name=name
        self.year=year
    def displayseries(self):
        print(f'Series name:{self.name}\nyear:{self.year}')
class Director(Series):
    def __init__(self,name,year,director):
        super().__init__(name,year)
        self.director=director
    def displaydirector(self):
        print(f'Director:{self.director}')
class Actors(Director):
    def __init__(self,name,year,director,actor):
        super().__init__(name,year,director)
        self.actor=actor
    def displayactor(self):
        self.displayseries()
        self.displaydirector()
        print(f'Actor:{self.actor}')
name=input('enter name')
year=int(input('enter year'))
director=input('enter director')
actor=input('enter actor')
obj=Actors(name,year,director,actor)
obj.displayactor()
