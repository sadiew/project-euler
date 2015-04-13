def is_prime(num):
	if num < 2:
		return False
	elif num == 2:
		return True
	elif num%2==0:
		return False
	else:
		sqrt = int(num**0.5) +1
		for i in range(3, sqrt,2):
			if num%i==0:
				return False
		return True

def solve_euler3(num):

	"""The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?"""

	all_factors = []
	for i in range(2,int(num**0.5+1)):
		if num % i == 0:
			all_factors.extend([i, num/i])

	all_factors.sort()
	all_factors.reverse()

	for num in all_factors:
		if is_prime(num) == True:
			return num

print solve_euler3(600851475143)
