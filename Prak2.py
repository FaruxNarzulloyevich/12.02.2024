class Car:
    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year

class SuperCar(Car):
    def __init__(self,model,color,year,sponsor):
        super().__init__(model,color,year)
        self.sponsor = sponsor

f1 = SuperCar('Honda','black',2024,'Farux')

print(f1.sponsor)