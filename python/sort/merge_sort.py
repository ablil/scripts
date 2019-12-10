def _merge_array(arr1, arr2):
	'''
	given two array arr1 & arr2, compare items from both of them & store their value
	on a new array in increasing order.
	By default arr1 & arr2 should sorted
	example : arr1 = [1,52,625]
			  arr2 = [0,55,100]
			  return value : [0, 1, 52, 55, 100, 625]
	'''
	res = list() # return value
	n1, n2 = len(arr1), len(arr2)
	i, j = 0, 0

	while i < n1 and j < n2:
		if arr1[i] > arr2[j]:
			res.append(arr2[j])
			j += 1
		else :
			res.append(arr1[i])
			i += 1

	# if some items remains on one of the array, simply copy them to return value array
	# they are by default sorted ( as supposed to be )
	if i < n1:
		while i < n1:
			res.append(arr1[i])
			i += 1

	if j < n2 :
		while j < n2 :
			res.append(arr2[j])
			j += 1

	return res

def merge_sort(array):
	'''
	merge sort is an algorithm based on devide & rule
	one of the most respected algorithm
	This function is recurisve.
	algorithm concept :
		step 1 : devide array into two array A & B
		step 2 : sort A & B using merge sort
		step 3 : merge A & b, then return it
	complexity : o( n * log n )
	'''
	if len(array) <= 1:
		# if array contains one items, there is nothing to sort
		# simply return array
		return array
	else :
		n = len(array)
		A = merge_sort(array[:n//2])
		B = merge_sort(array[n//2:])

		return _merge_array(A, B)
