import numpy as np
import matplotlib.pyplot as plt
import math


def draw_lines(f: (), x, y, lines):
    x = np.linspace(x[0], x[1], math.ceil(20*(x[1] - x[0])))
    y = np.linspace(y[0], y[1], math.ceil(20*(y[1] - y[0])))

    X, Y = np.meshgrid(x, y)
    Z = [[f((X[i][j], Y[i][j])) for j in range(x.size)] for i in range(y.size)]
    plt.contour(X, Y, Z)
    for i in range(len(lines) - 1):
        plt.plot([-lines[i][0], -lines[i + 1][0]], [-lines[i][1], -lines[i + 1][1]])
    plt.show()
