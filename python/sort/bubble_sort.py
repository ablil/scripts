def bubble_sort(array):
	'''
	create copy of array, sort it then return it without changing the original array
	algorithm concept :

		step 1: compare two element array[i] and array[i +
		1] starting from i = 0
			if array[i] > array[i + 1] then swap, else do nothing
		step 2 : increase i
				repeat step 1 again
		step 3 : repeat step 1 and step until we cannot swa[]

	complexity : o(n * n) where n is the number of item on array
	'''

	duplicate_array = array; # create copy of array to work with
	swap_counter = True # set swap_counter of swaping process, set swap_counter = True to enter the while loop

	while swap_counter:
		# each while loop, we go through the whole array & set swap_counter to true if we swapped
		swap_counter = False
		for i in range(len(duplicate_array) - 1):
			if duplicate_array[i] > duplicate_array[i + 1]:

				# swap
				duplicate_array[i], duplicate_array[i+1] = duplicate_array[i+1], duplicate_array[i]

				# set swap_counter = True, wich means we've swaped somthing
				swap_counter = True

	# return duplicate_array after sorting it
	return duplicate_array
