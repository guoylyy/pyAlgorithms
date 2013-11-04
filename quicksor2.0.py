def quicksort(a):
	"""
	use quicksort to sort a list
	input: list a
	output: list a in non-descending order
	"""
	if not a:
		return []
	return quicksort([x for x in a[1:] if x < a[0]]) +\
                a[0:1] +\
                quicksort([x for x in a[1:] if x >= a[0]])

if __name__ == '__main__':
	a = [99,34,1,2,3,5,365,-123,345]
	print(quicksort(a))
