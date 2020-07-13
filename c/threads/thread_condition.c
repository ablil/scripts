#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;


int generate_random(){ 
    return (rand() % 200 - 0 + 1);
}

void *consumer(void *arg) {

    printf("Consumer started\n");

    pthread_mutex_lock(&lock);
    printf("wating for condition...\n");
    pthread_cond_wait(&cond, &lock);
    printf("condition is true, variable is above 100\n");
    pthread_mutex_unlock(&lock);

    printf("Consumer ended\n");
}


void *producer(void *arg) {


    printf("Producer started\n");

    for (int i = 0; i < 1000000; i++) {
        int number = generate_random();
        printf("%d ", number);
        if ( number > 100 ) {
            pthread_cond_broadcast(&cond);
            break;
        }
    }

    printf("Producer finished\n");
}

int main() {

    srand(time(NULL));
    
    pthread_t producer_thread;
    pthread_t consumer_thread;

    // start consumer thread
    pthread_create(&consumer_thread, NULL, consumer, NULL);

    // start producer thread
    pthread_create(&producer_thread, NULL, producer, NULL);

    // wiat for threads to finish
    pthread_join(consumer_thread, NULL);
    pthread_join(producer_thread, NULL);

    // dipslay exit status
    printf("\nProgram finished\n");
    return 0;
}
