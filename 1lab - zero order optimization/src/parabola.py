def parabola(leftBorder: float, rightBorder: float, accuracy: float, function: ()):

	# calculate inner point
	x = (leftBorder + rightBorder) / 2

	fl = function(leftBorder)
	fx = function(x)
	fr = function(rightBorder)

	# variables storing the number of iterations and calculations of the function, respectively
	iterations = 0
	calculations = 3

	# array of segment lengths
	uncertainlySegmentLength = []

	while True:

		iterations += 1
		uncertainlySegmentLength.append(rightBorder - leftBorder)

		u = x - 0.5 * ((x - leftBorder) ** 2 * (fx - fr) - (x - rightBorder) ** 2 * (fx - fl)) / ((x - leftBorder) * (fx - fr) - (x - rightBorder) * (fx - fl))
		fu = function(u)

		calculations += 1

		if abs(u - x) < accuracy:
			if fu > fx:
				xMin = x
				fxMin = fx
				break
			else:
				xMin = u
				fxMin = fu
				break

		if fu < fx:

			if u >= x:
				leftBorder = x
				fl = fx
				x = u
				fx = fu
			else:
				rightBorder = x
				fr = fx
				x = u
				fx = fu

		elif fu > fx:

			if u >= x:
				rightBorder = u
				fr = fu
			else:
				leftBorder = u
				fl = fu

		else:

			leftBorder = u
			fl = fu
			x = (leftBorder + rightBorder) / 2
			fx = function(x)

			calculations += 1

	print("__Parabola method__")
	print(f"X coordinate of the found minimum point: {xMin}")
	print(f"Y coordinate of the found minimum point: {fxMin}")
	print(f"Number of iterations: {iterations}")
	print(f"Number of function calculations: {calculations}")
	print(f"Сhange in uncertainty interval: {uncertainlySegmentLength}")