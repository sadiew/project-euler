def is_palindrome(num):
	forward_counter = 0
	backward_counter = -1

	num_string = str(num)
	for i in range(len(num_string)/2):
		if num_string[forward_counter] == num_string[backward_counter]:
			forward_counter += 1
			backward_counter -= 1
		else:
			return False

	return True

print is_palindrome(9009)

def solve_euler4():
	"""Find the largest palindrome made from the product of two 3-digit numbers."""
	
	palindromes = []	
	for i in range(999,99, -1):
		for j in range(999,99, -1):
			if is_palindrome(i*j) == True:
				palindromes.append(i*j)
	palindromes.sort()
	print palindromes
	return palindromes[-1]
print solve_euler4()

