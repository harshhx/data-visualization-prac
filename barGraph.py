import matplotlib.pyplot as plt
import numpy

x_coordinates= numpy.array([1, 2, 3]) * 2

plt.bar(x_coordinates, [10, 20, 30], width=0.5, label="current year", tick_label=["gold", "silver", "diamond"])
plt.bar(x_coordinates + 0.5, [15, 25, 18], width=0.5, label="past year", tick_label=["gold", "silver", "diamond"])
plt.legend()
plt.show()
