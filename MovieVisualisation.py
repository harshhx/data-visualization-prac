import pandas
import numpy
import matplotlib.pyplot as plt
df = pandas.read_csv("movieData.csv")
titles = list(df.get("movie_title"))
freq_titles ={}
for t in titles:
    length = len(t)
    if freq_titles.get(length) is None:
        freq_titles[length] = 1
    else:
        freq_titles[length] += 1

X = numpy.array(list(freq_titles.keys()))
Y = numpy.array((list(freq_titles.values())))
plt.scatter(X,Y)
plt.xlabel("Length of Movie")
plt.ylabel("frequency of movies")
plt.title("Movie Data Visualisation")
plt.show()

