from human_class import Human
from robot_class import Robot

class Planet:

    def __inti__(self, name):
        self.humans = []
        self.robots = []
        self.name = name

    def add_human(self,human):
        self.humans += human

    def remove_human(self,human):
        if human in self.humans:
            self.humans.remove(human)
