import matplotlib.pyplot as plt


def coordinate():
    x = int(input("enter a x value"))
    y = int(input("enter a x value"))
    return x, y


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(0, 4):
        x_values, y_values = coordinate()
    return [x_values, y_values]


def run_task3():
    values = path()
    plt.plot(values[0], values[1], "ro--")
    plt.show()


if __name__ == "__main__":
    run_task3()
