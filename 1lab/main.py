from dichotomy import dichotomy
from goldenRatio import goldenRatio
from function import function

if __name__ == '__main__':

    leftBorder = 2
    rightBorder = 7
    accuracy = 0.01

    dichotomy(leftBorder = leftBorder, rightBorder = rightBorder, accuracy = accuracy, function = function)
    goldenRatio(leftBorder = leftBorder, rightBorder = rightBorder, accuracy = accuracy, function = function)