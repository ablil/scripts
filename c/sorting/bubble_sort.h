#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b){
 int temp = *a;
 *a = *b;
 *b = temp;
}

void display_array(int *array, int n ){
    printf("array elements : ");
    for (int i = 0; i < n; i++ ){
        printf("%d, ", array[i]);
    }
    printf("\n");
}

void bubble_sort(int *array, int n) {
    int counter = 1;
    while ( counter ) {
        counter = 0;
        for (int i = 0; i < n-1; i++) {
            if ( array[i] >  array[i+1]) {
                swap(array + i, array + i +1);
                counter = 1;
            }
        }
    }
}

