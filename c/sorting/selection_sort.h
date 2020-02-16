#include <stdio.h>
#include <stdlib.h>

void selection_sort(int *array, int n) {
    for (int i =0 ; i < n -1; i++){
        int imin = i;
        int j = i;
        while ( j < n ){
            if ( array[j] < array[imin]){
                imin = j;
            }
            j++;
        }
        if ( imin != i ) {
            // swap the values
            int tmp = *(array + i);
            *(array + i ) = *(array + imin);
            *(array + imin) = tmp;
        }
    }
}