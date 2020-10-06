import matplotlib.pyplot as plt
import numpy

x = numpy.arange(10)
y = x**2 - 4*x - 2
z = 2*x**2 + 10

# plt.title("graphs of the lines")
# plt.plot(x,y,label ="x**2 - 4*x - 2")
# plt.plot(x,z,label="2*x**2 + 10")
# plt.axis("off")
# plt.legend()
# plt.show()

plt.title("graphs of the lines")
plt.scatter(x,y,label ="x**2 - 4*x - 2")
plt.scatter(x,z,label="2*x**2 + 10")
plt.axis("off")
plt.legend()
plt.show()