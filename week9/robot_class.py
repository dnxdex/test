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
