def dichotomy(leftBorder: float, rightBorder: float, accuracy: float, function: ()):

    # variables storing the number of iterations and calculations of the function, respectively
    iterations = 0
    calculations = 0

    # coefficient reflects how large the indents from the midpoint will be (from 0 (coeff = 0) to accuracy / 2 (coeff = 1))
    indentCoeff = 0.7

    # indent from the midpoint
    delta = (accuracy / 2) * indentCoeff

    # array of segment lengths
    uncertainlySegmentLength = [rightBorder - leftBorder]

    # reduce the segment until we reach the specified accuracy
    while abs(rightBorder - leftBorder) > accuracy:

        x1 = (leftBorder + rightBorder) / 2 - delta
        x2 = (leftBorder + rightBorder) / 2 + delta

        # change the boundaries of the segment of uncertainty
        if function(x1) > function(x2):
            leftBorder = x1
        elif function(x1) < function(x2):
            rightBorder = x2
        else:
            leftBorder = x1
            rightBorder = x2

        iterations += 1
        calculations += 2

        uncertainlySegmentLength.append(rightBorder - leftBorder)

    print("__Dichotomy method__")
    print(f"X coordinate of the found minimum point: {(leftBorder + rightBorder) / 2}")
    print(f"Y coordinate of the found minimum point: {function((leftBorder + rightBorder) / 2)}")
    print(f"Number of iterations: {iterations}")
    print(f"Number of fuction calculations: {calculations + 1}")
    print(f"Сhange in uncertainty interval: {uncertainlySegmentLength}")
