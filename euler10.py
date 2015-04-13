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

def solve_euler10(upper_bound):
	primes_sum = 5

	i = 4
	while i < upper_bound:
		if is_prime(i) == True:
			primes_sum += i
		i += 1
	return primes_sum

print solve_euler10(2000000)