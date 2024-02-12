class Animal:
    def make_sound(self, s):
        print(s)

class Horse(Animal):
    pass

pony = Horse()
pony.make_sound('Yohuu')