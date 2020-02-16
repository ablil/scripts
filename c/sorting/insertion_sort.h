#include <stdio.h>
#include <stdlib.h>

void display_array(int *array, int n ){
    printf("array elements : ");
    for (int i = 0; i < n; i++ ){
        printf("%d, ", array[i]);
    }
    printf("\n");
}

void insertion_sort(int *array, int n) {
    int i;
    for (i = 0 ; i < n; i++){
        int m = array[i];
        int j = i;
        while ( j > 0 && array[j-1] > m ){
            array[j] = array[j-1];
            j--;
        }
        array[j] = m;
    }
}