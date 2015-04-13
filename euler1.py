def solve_euler1():

	"""If we list all the natural numbers below 10 that are multiples of 3 or 5, 
	we get 3, 5, 6 and 9. The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000."""
	
	multiples3_and5 = []
	for i in range(1000):
		if i%3 == 0 or i%5 ==0:
			multiples3_and5.append(i)

	list_sum = 0
	for num in multiples3_and5:
		list_sum += num

	return list_sum

print solve_euler1()