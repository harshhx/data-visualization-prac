import numpy as np
import matplotlib.pyplot as plt

x = np.array([i**2 for i in range(10)])
y = x**2+3
plt.style.use("dark_background")
plt.plot(x,y,label="stock price on monday")
plt.title("my line")
plt.plot(x,y*3,label="stock price on tuesday")
plt.xlabel("timestamp")
plt.ylabel("price")
plt.legend()
plt.show()