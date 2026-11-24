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

    def increase_age(self):
        self.age += 1

    def increase_energy(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100

    def move(self, distance):
        if self.energy - distance > 0:
            self.energy -= distance
        else:
            self.energy = 0
