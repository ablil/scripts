def insertion_sort(array):
	'''
	create copy of array, sort it then return it witout chaning the original array
	algorithm concept :
		step 1 : take element from array with index i
			search the appropriate place
		step 2  : insert in appropriate place
		step 3 : increase i
		step 3 : return to step 1 while i < number of items
	complexity : o(n * n) where n is the number of item on array
	'''

	duplicate_array = array # create duplicate array to work with
	n = len(duplicate_array)

	for i in range(n):
		m = duplicate_array[i]
		j = i

		'''
		find appropriate place for m = duplicate_array[i] by shifting all on left of m to the right
		until we reach an element with index j where duplicate_array[j] < m
		then insert m on that place
		'''
		while j > 0 and duplicate_array[j -1] > m :
			duplicate_array[j] = duplicate_array[j -1]
			j -= 1
		duplicate_array[j] = m

	# return duplicate_array after sorting it
	return duplicate_array
