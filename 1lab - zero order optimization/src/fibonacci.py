def fibonacci(leftBorder: float, rightBorder: float, accuracy: float, function: ()):

	# array of segment lengths
	uncertainlySegmentLength = [rightBorder - leftBorder]

	# fill array of fibonacci values
	# the number of values needed to achieve the specified accuracy
	fibonacci = [1, 1]
	index = 1
	while (rightBorder - leftBorder) / accuracy > fibonacci[index]:
		index += 1
		fibonacci.append(fibonacci[index - 1] + fibonacci[index - 2])

	# number of iterations
	iterations = len(fibonacci) - 1

	# calculate first two dots
	x1 = leftBorder + (rightBorder - leftBorder) * (fibonacci[iterations - 2]/ fibonacci[iterations])
	x2 = leftBorder + (rightBorder - leftBorder) * (fibonacci[iterations - 1]/ fibonacci[iterations])
	fx1 = function(x1)
	fx2 = function(x2)

	# number of function calculations
	calculations = 2

	for k in range(1, iterations):
		
		if fx1 > fx2:
			leftBorder = x1
			x1 = x2
			fx1 = fx2

			x2 = leftBorder + (fibonacci[iterations - k - 1] / fibonacci[iterations - k]) * (rightBorder - leftBorder)
			fx2 = function(x2)

		else:
			rightBorder = x2
			x2 = x1
			fx2 = fx1

			x1 = leftBorder + (fibonacci[iterations - k - 2] / fibonacci[iterations - k]) * (rightBorder - leftBorder)
			fx1 = function(x1)

		calculations += 1
		uncertainlySegmentLength.append(rightBorder - leftBorder)

	print("__Fibonacci method__")
	print(f"X coordinate of the found minimum point: {(leftBorder + rightBorder) / 2}")
	print(f"Y coordinate of the found minimum point: {function((leftBorder + rightBorder) / 2)}")
	print(f"Number of iterations: {iterations}")
	print(f"Number of function calculations: {calculations + 1}")
	print(f"Сhange in uncertainty interval: {uncertainlySegmentLength}")