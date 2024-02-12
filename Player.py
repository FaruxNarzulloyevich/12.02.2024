class Player:
    def __init__(self, stanina, accuracy, speed, power):
        self.stanina = stanina
        self.accuracy = accuracy
        self.speed = speed
        self.power = power


class Atcker(Player):
    def __init__(self, stanina, accuracy, speed, power, ):
        super().__init__(stanina, accuracy, speed, power)
    def goal(self):
        return 'Zabil goll!!!'

class Goalkeeper(Player):
    def __init__(self, stanina, accuracy, speed, power, ):
        super().__init__(stanina, accuracy, speed, power)

    def catch(self):
        return 'Poymal myach!!!'

mbappe = Player(100,100,100,100)
print(vars(mbappe))