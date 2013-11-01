def binary_search(a, k):
	"""
	implement non-recursive binary_search
	input: list a, k
	output: the position of k; or -1(can not find k)
	"""
	l = 0
	r = len(a) - 1
	while l <= r:
		m = (l + r) / 2

		if a[m] == k:
			return k
		elif k < a[m]:
			r = m - 1
		else:
			l = m + 1

	# can not find k in list a		
	return -1
