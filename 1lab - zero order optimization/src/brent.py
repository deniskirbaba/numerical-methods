from math import sqrt

def brent(leftBorder: float, rightBorder: float, accuracy: float, function: ()):

    # golden ratio coefficient
    phi = (3 - sqrt(5)) / 2

    # initial values of our dots
    x = w = v = (leftBorder + rightBorder) / 2
    fx = fw = fv = function(x)

    u = 0

    # variables to store the lengths of the previous and prev-previous steps of the algorithm
    prev = prevprev = rightBorder - leftBorder

    # variables storing the number of iterations and calculations of the function, respectively
    iterations = 0
    calculations = 1

    # array of segment lengths
    uncertainlySegmentLength = []

    while True:

        iterations += 1
        uncertainlySegmentLength.append(rightBorder - leftBorder)

        # at each iteration, we either use the parabola method or the golden section method
        # this variable allows only one of the methods to be executed
        goldenRatioFlag = True

        # if x, w, v are different, then we build an approximating parabola
        if (x != w != v) and (fx != fw != fv):
            u = x - 0.5 * ((x - v) ** 2 * (fx - fw) - (x - w) ** 2 * (fx - fv)) / ((x - v) * (fx - fw) - (x - w) * (fx - fv))
            
            # check if the found minimum is in our segment and far from the boundaries and
            # is no more than half the length of the prev-previous step from the point x
            if abs(u - x) < prevprev / 2 and ((leftBorder + accuracy) <= u <= (rightBorder - accuracy)):
                goldenRatioFlag = False
                prev = abs(u - x)

        # else use the golden ration method
        if goldenRatioFlag:
            if x < (rightBorder + leftBorder) / 2:
                u = x + phi * (rightBorder - x)
                prev = rightBorder - x
            else:
                u = x - phi * (x - leftBorder)
                prev = x - leftBorder

        fu = function(u)
        calculations += 1

        # check for an stop condition
        if rightBorder - leftBorder < accuracy:
            if fu > fx:
                xMin = x
                fxMin = fx
                break
            else:
                xMin = u
                fxMin = fu
                break

        if fu <= fx:

            if u >= x:
                leftBorder = x
            else:
                rightBorder = x

            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu

        else:

            if u >= x:
                rightBorder = u
            else:
                leftBorder = u

            if fu <= fw and w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <= fv and v == x and v == w:
                v = u
                fv = fu

        # save the prev-previous value
        prevprev = prev

    print("__Brent's method__")
    print(f"X coordinate of the found minimum point: {xMin}")
    print(f"Y coordinate of the found minimum point: {fxMin}")
    print(f"Number of iterations: {iterations}")
    print(f"Number of function calculations: {calculations}")
    print(f"Сhange in uncertainty interval: {uncertainlySegmentLength}")