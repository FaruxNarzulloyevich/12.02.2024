class Math:
    def __init__(self,value):
        self.value = value


    @classmethod
    def multiply(cls, value):
        return cls(value * 2)

print(Math.multiply(10).value)