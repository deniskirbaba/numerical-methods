from dichotomy import dichotomy
from goldenRatio import goldenRatio
from fibonacci import fibonacci
from parabola import parabola
from brent import brent
from function import function

if __name__ == '__main__':

    leftBorder = 2
    rightBorder = 7
    accuracy = 0.01

    dichotomy(leftBorder = leftBorder, rightBorder = rightBorder, accuracy = accuracy, function = function)
    goldenRatio(leftBorder = leftBorder, rightBorder = rightBorder, accuracy = accuracy, function = function)
    fibonacci(leftBorder = leftBorder, rightBorder = rightBorder, accuracy = accuracy, function = function)
    parabola(leftBorder = leftBorder, rightBorder = rightBorder, accuracy = accuracy, function = function)
    brent(leftBorder = leftBorder, rightBorder = rightBorder, accuracy = accuracy, function = function)