def solve_euler12():
	"""The sequence of triangle numbers is generated by adding the natural numbers. 
	So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

	1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

	Let us list the factors of the first seven triangle numbers:

	 1: 1
	 3: 1,3
	 6: 1,2,3,6
	10: 1,2,5,10
	15: 1,3,5,15
	21: 1,3,7,21
	28: 1,2,4,7,14,28
	We can see that 28 is the first triangle number to have over five divisors.

	What is the value of the first triangle number to have over five hundred divisors?"""

	next_triangular_num = 0
	triangular_nums = {}

	for i in range(1, 13000):
		next_triangular_num += i
		triangular_nums[next_triangular_num] = sorted(find_factors(next_triangular_num))

	#print triangular_nums

	number_of_factors = {}
	for num in sorted(triangular_nums):
		number_of_factors[num] = len(triangular_nums[num])

	#print max(number_of_factors.values())

	over_500 = []
	for num in number_of_factors:
		if number_of_factors[num] > 500:
			over_500.append((num, number_of_factors[num]))
	print over_500


def find_factors(num):
	all_factors = [1, num]
	for i in range(2,int(num**0.5+1)):
		if num % i == 0:
			all_factors.extend([i, num/i])
	return all_factors

solve_euler12()
