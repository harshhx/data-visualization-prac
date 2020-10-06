import numpy
import matplotlib.pyplot as plt

Xsn = numpy.random.randn(100)
sigma = 8
mean = 70
X = numpy.round(Xsn*sigma + mean)
plt.style.available()
plt.hist(X)
plt.show()