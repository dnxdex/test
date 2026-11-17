import matplotlib.pyplot as plt


x = [1, 1, 6, 6, 1]
y = [1, 6, 6, 1, 1]
plt.plot(x, y, 'x-')

x = [2, 5, 5, 2, 2]
y = [5, 5, 2, 2, 5]
plt.plot(x, y, "gs-")

x = [3, 3, 4, 4, 3]
y = [3, 4, 4, 3, 3]
plt.plot(x, y, 'ro--')
plt.show()
