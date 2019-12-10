def _partition(sequence, low, high):
    pivot = sequence[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if sequence[j] < pivot:
            sequence[j], sequence[i] = sequence[i], sequence[j]
            i += 1
    sequence[i-1], sequence[low] = sequence[low], sequence[i-1]
    return i - 1

def quick_sort(sequence, low, high):
    '''
    sort the given array (sequence)
    low : should be set to 0
    high : soudl be set to len(sequence ) -1

    algorithm concept :
    Step 1 − Choose the highest index value has pivot
    Step 2 − Take two variables to point left and right of the list excluding pivot
    Step 3 − left points to the low index
    Step 4 − right points to the high
    Step 5 − while value at left is less than pivot move right
    Step 6 − while value at right is greater than pivot move left
    Step 7 − if both step 5 and step 6 does not match swap left and right
    Step 8 − if left ≥ right, the point where they met is new pivot

    complexity : o (n * n ) where n is the number of elements.
    '''

    if low < high:
        pivot = _partition(sequence, low, high)
        quick_sort(sequence, low, pivot - 1)
        quick_sort(sequence, pivot + 1, high)
