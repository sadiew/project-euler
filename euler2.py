def solve_euler2():

	"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
	By starting with 1 and 2, the first 10 terms will be:

	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

	By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
	find the sum of the even-valued terms."""

	fibonacci_numbers = [1,2]

	i=2
	while fibonacci_numbers[-1] < 4000000:
		next_num = fibonacci_numbers[i-2] + fibonacci_numbers[i-1]
		fibonacci_numbers.append(next_num)
		i+=1

	even_sum = 0
	for num in fibonacci_numbers:
		if num%2==0:
			even_sum += num
	return even_sum

print solve_euler2()