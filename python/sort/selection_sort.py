def selection_sort(array):
	'''
	create copy of array, sort it then return it without changing the original array
	algorithm concept :
		Step 1 : Set MIN to location 0
		Step 2 : Search the minimum element in the list
		Step 3 : Swap with value at location MIN
		Step 4 : Increment MIN to point to next element
		Step 5 : Repeat until list is sorted
	complexity : o( n * n )
	'''
	duplicate_array = array # create copy of array to work with
	n = len(duplicate_array)

	for i in range(n-1):
		imin = i
		j = i
		while j < n :
			if duplicate_array[j] < duplicate_array[imin] :
				imin = j
			j += 1

		if imin != i:
			duplicate_array[i], duplicate_array[imin] = duplicate_array[imin], duplicate_array[i]

	# return duplicate_array after sorting it
	return duplicate_array
