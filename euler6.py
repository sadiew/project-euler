def solve_euler6():

	"""Find the difference between the sum of the squares of the first one hundred natural numbers 
	and the square of the sum."""

	sum_of_naturals = 0
	sum_of_squares = 0

	for i in range(1,101):
		sum_of_naturals += i
		sum_of_squares += (i**2)

	return ((sum_of_naturals)**2 - sum_of_squares)

print solve_euler6()


