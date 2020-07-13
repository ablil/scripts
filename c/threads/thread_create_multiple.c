#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <pthread.h>

void *callback(void *arg) {
    printf("Thread called with varaible: %d\n", *((int*) arg));

    printf("Process id: %d\n", getpid());

    printf("Thread loop started\n");
    for (int i = 0; i < 100; i++);
    printf("Thread loop ended\n\n");
}

int main() {

    pthread_t threads_id[20];

    // create multiple threads (thread start runnint once created)
    int status;
    for (int i = 0; i < 20; i++) {
        status = pthread_create(&threads_id[i], NULL, callback, (void*) &i);
        printf("Thread status %s\n", (status == 0)? "success" : "fail");
    }

    // wait for all threads to finish then continue execution
    for (int i = 0; i < 20; i++)
        pthread_join(threads_id[i], NULL);
    printf("Main programm conitnue execution\n");
    printf("Main process id: %d\n", getpid());

    return 0;
}



