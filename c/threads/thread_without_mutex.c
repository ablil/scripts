#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/types.h>
#include <unistd.h>


int shared_variable = 10;

void *consumer(void *arg) {

    printf("Consumer started\n");

    for (int i = 0; i < 1000000; i++) {
        shared_variable--;
        printf("Consumer running %d\n", shared_variable);
    }

    printf("Consumer finished\n");
}

void *producer(void *arg) {

    printf("Producer started\n");

    for (int i = 0; i < 1000000; i++) {
        shared_variable++;
        printf("Producer running %d\n", shared_variable);
    }

    printf("Producer finished\n");
}

int main() {


    printf("\nInitial shared value: %d\n\n", shared_variable);

    pthread_t producer_thread;
    pthread_t consumer_thread;

    // create threads
    pthread_create(&producer_thread, NULL, producer, NULL);
    pthread_create(&consumer_thread, NULL, consumer, NULL);


    // join threads
    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);


    // continue execution
    printf("\nFinal shared value: %d\n", shared_variable);


    return 0;
}
