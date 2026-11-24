class Human:
    def __init__(self):
        self.MAX_ENERGY = 100
        self.name = "human"
        self.age = 0
        self.energy = self.MAX_ENERGY

    def displayname(self):
        return self.name

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'