def euclid(m, n):
	"""
	calculate gcd(m, n) using euclid algorithm
	input: two non-negative numbers, they do not equal 0 at the same time
	output: gcd(m, n)
	"""
	while n != 0:
		r = m % n
		m = n
		n = r
	return m

# test 
if __name__ == '__main__':
	m = 52346536
	n = 12341212
	print euclid(m, n)
