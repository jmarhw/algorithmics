import numpy as np
import matplotlib.pylab as plt


#PageRank is an algorithm used by google Search to rank web pages

n=6
Pg = np.array([[0, 0, 0, 0.5, 0.5, 0],
               [0, 0, 0.5, 0, 0.0, 0.5],
               [0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0],
               [0, 0.5, 0, 0.5, 0, 0],
               [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]])

Jm=np.array([[1]*n]*n)

alfa = 1
for a in np.arange(0, alfa, 0.05):
    Mg = (1 - a) * Pg + (a / n) * Jm
    Mgmul = np.matmul(Mg, Mg)
    for b in range(0, 1000):
        Mgmul = np.matmul(Mgmul, Mg)
    c = Mgmul[0]
    plt.figure(1)
    plt.subplot(1, 2, 1)
    c1 = plt.scatter(a, c[0], color="red")
    c2 = plt.scatter(a, c[1], color="blue")
    c3 = plt.scatter(a, c[2], color="yellow")
    c4 = plt.scatter(a, c[3], color="orange")
    c5 = plt.scatter(a, c[4], color="pink")
    c6 = plt.scatter(a, c[5], color="green")
    plt.legend((c1, c2, c3, c4, c5, c6), ("A", "B", "C", "D", "E", "F"))

Pg = np.array([[0, 0, 0, 0.5, 0.5, 0],
               [0, 0, 0.5, 0, 0.0, 0.5],
               [0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0],
               [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]])

for a in np.arange(0, alfa, 0.05):
    Mg = (1 - a) * Pg + (a / n) * Jm
    Mgmul = np.matmul(Mg, Mg)
    for b in range(0, 1000):
        Mgmul = np.matmul(Mgmul, Mg)
    c = Mgmul[0]
    plt.subplot(1, 2, 2)
    c1 = plt.scatter(a, c[0], color="red")
    c2 = plt.scatter(a, c[1], color="blue")
    c3 = plt.scatter(a, c[2], color="yellow")
    c4 = plt.scatter(a, c[3], color="orange")
    c5 = plt.scatter(a, c[4], color="pink")
    c6 = plt.scatter(a, c[5], color="green")
    plt.legend((c1, c2, c3, c4, c5, c6), ("A", "B", "C", "D", "E", "F"))
plt.suptitle("α=0.5")
plt.show()
