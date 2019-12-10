def shell_sort(array):
    '''
    create copy of array, sort it then return it witout changing the original one
    algorithm concept :
    step 1 : initialize the value of interval
    step 2 : divide the list into smaller sub-list of equal interval
    step 3 : sort these sub-lists using insertion sort
    step 4: repeat until complete list is sorted

    the interval is calculated based on Knuth's fomula
    h = h * 3 + 1
    here -
        h is interval with initial value 1

    complexity : o(n) where n is number of elements
    '''

    duplicate_array = array
    n = len(array)
    interval = 1

    # calculate interval
    while interval < n //3 :
        interval = interval * 3 + 1

    while interval > 0 :
        for outer in range(interval, n):

            # select value to insert
            value_to_insert = duplicate_array[outer]
            inner = outer

            # shift element toward right
            while inner > interval -1 and duplicate_array[inner - interval] >= value_to_insert :
                duplicate_array[inner] = duplicate_array[inner  - interval ]
                inner = inner - interval

            # insert the number at hole position
            duplicate_array[inner] = value_to_insert

        # calculate interval
        interval = (interval - 1) // 3;

    # return array after sorting it
    return duplicate_array
