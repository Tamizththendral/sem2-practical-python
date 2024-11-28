class Books:
    def __init__(self,name,author=6677,amount=500):
        self.name=name
        self.author=author
        self.amount=amount
    def show(self):
        print('Books:', self.name,self.author,self.amount)
book1=Books('harry potter')
book1.show() 
