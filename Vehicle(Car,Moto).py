class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def display_info(self,s):
        print(s)

class Car(Vehicle):
    def __init__(self,brand,year,type,color):
        super().__init__(brand,year)
        self.type = type
        self.color = color
    def display_info(self):
        return (Auto.brand,Auto.year,Auto.type,Auto.color)

class Motorcycle(Vehicle):
    def __init__(self,brand,year,power,speed):
        super().__init__(brand,year)
        self.power = power
        self.speed = speed
    def display_info(self):
        return (Moto.brand,Moto.year,Moto.power,Moto.speed)
a = input('Kakoy transport? ')
if a.lower() == 'auto':
    ab = str(input('Vvedite bren: '))
    ac = input('Vedite god vipuska: ')
    ad = str(input('Vvedite tip: '))
    ae = input('Vvedite svet: ')
    Auto = Car(brand=ab,year=ac,type=ad,color=ae)
    print(Auto.display_info())
elif a.lower() == 'moto':
    ab = str(input('Vvedite bren: '))
    ac = input('Vedite god vipuska: ')
    ad = input('Vvedite power: ')
    ae = input('Vvedite max skorost: ')
    Moto = Motorcycle(brand=ab,year=ac,power=ad,speed=ae)
    print(Moto.display_info())
else:
    print("Ne ponel😎😎")
