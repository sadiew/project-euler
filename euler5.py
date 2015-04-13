def solve_euler5():
	
	"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

	multiples_20 = range(20, 20*19*18*17*16*14*13, 20)

	for num in multiples_20:
		if num % 19 == 0 and num % 18 ==0 and num % 17 ==0 and num % 16 ==0 and num % 14 ==0 and num % 13 ==0 and num % 11 ==0:
			return num

print solve_euler5()


