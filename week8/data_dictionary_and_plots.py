import matplotlib.pyplot as plt
from random import sample


def data():
    path = {}
    line_type = input("What line would you like. :, -, --")
    line_color = input("What color would you like. r, g, b")
    line_marker = input("What color would you like. o, s, ^")
    path["type"] = line_type
    path["color"] = line_color
    path["marker"] = line_marker
    return path


def generate():
    lime_amount = int(input("How many lines would you like to display?"))
    list = [10, 20, 30, 40, 50]
    for i in range(lime_amount):
        values = data()
        print(values["type"], values["color"], values["marker"])
        print(sample(list,3))
        print(sample(list,3))

        plt.plot(sample(list, 3), sample(list, 3), color=values["color"], marker=values["marker"], linestyle=values["type"])
        plt.show()


generate()
