#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <pthread.h>

void *callback(void *arg) {
    printf("Thread called with varaible: %s\n", (const char*) arg);

    printf("Process id: %d\n", getpid());

    printf("Thread loop started\n");
    for (int i = 0; i < 100; i++);
    printf("Thread loop ended\n");
}

int main() {

    pthread_t thread_id;

    // create thread (thread start runnint once created)
    int status = pthread_create(&thread_id, NULL, callback, "variable");
    printf("Thread status %s\n", (status == 0)? "success" : "fail");

    // wiat for the thread to finish, then continue the programm execution
    pthread_join(thread_id, NULL);
    printf("Main programm conitnue execution\n");
    printf("Main process id: %d\n", getpid());

    return 0;
}



