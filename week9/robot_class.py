class Robot:
    def __init__(self):
        self.MAX_ENERGY = 100
        self.name = "robot"
        self.age = 0
        self.energy = 0

    def displayname(self):
        return self.name

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

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