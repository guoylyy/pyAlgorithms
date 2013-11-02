import random
def quicksort(a):
	"""
	use quicksort to sort list a
	input: list a
	output: list a in non-descending order
	"""
	if len(a) <= 1:
		return a

	greater = []
	less = []
	# choose the value in random position as pivot
	pivot = a.pop(random.randint(0, len(a) - 1))
	for item in a:
		if(item < pivot):
			less.append(item)
		else:
			greater.append(item)

	return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
	a = [1,3,55,32,77645,1,-123,4,-3]
	print(quicksort(a))
	
