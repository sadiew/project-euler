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

def solve_euler7():
	"""Find the 1001st prime number.
	Example: 2,3,5,7,11,13 --> 13 is the 6th prime number"""

	prime_numbers = [2]
	i=3

	while len(prime_numbers) < 10001:
		if is_prime(i) == True:
			prime_numbers.append(i)
		i+=1
	#return len(prime_numbers)	
	return prime_numbers[10000]

print solve_euler7()

