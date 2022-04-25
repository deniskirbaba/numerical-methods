from math import sqrt

def goldenRatio(leftBorder: float, rightBorder: float, accuracy: float, function: ()):

	# golden ratio coefficients
	phi1 = (3 - sqrt(5)) / 2
	phi2 = (-1 + sqrt(5)) / 2

	x1 = leftBorder + (rightBorder - leftBorder) * phi1
	x2 = leftBorder + (rightBorder - leftBorder) * phi2

	fx1 = function(x1)
	fx2 = function(x2)

	# variables storing the number of iterations and calculations of the function, respectively
	iterations = 0
	calculations = 2

	# array of segment lengths
	uncertainlySegmentLength = [rightBorder - leftBorder]

	# reduce the segment until we reach the specified accuracy
	while abs(rightBorder - leftBorder) > accuracy:

		# change the boundaries of the segment of uncertainty
		if fx1 < fx2:
			rightBorder = x2
			x2 = x1
			fx2 = fx1
			x1 = leftBorder + (rightBorder - leftBorder) * phi1
			fx1 = function(x1)
		elif fx1 > fx2:
			leftBorder = x1
			x1 = x2
			fx1 = fx2
			x2 = leftBorder + (rightBorder - leftBorder) * phi2
			fx2 = function(x2)
		else:
			leftBorder = x1
			rightBorder = x2
			x1 = leftBorder + (rightBorder - leftBorder) * phi1
			x2 = leftBorder + (rightBorder - leftBorder) * phi2
			fx2 = function(x2)
			fx1 = function(x1)
			calculations += 1

		iterations += 1
		calculations += 1

		uncertainlySegmentLength.append(rightBorder - leftBorder)

	print("__Golden ratio method__")
	print(f"X coordinate of the found minimum point: {(leftBorder + rightBorder) / 2}")
	print(f"Y coordinate of the found minimum point: {function((leftBorder + rightBorder) / 2)}")
	print(f"Number of iterations: {iterations}")
	print(f"Number of fuction calculations: {calculations + 1}")
	print(f"Сhange in uncertainty interval: {uncertainlySegmentLength}")
