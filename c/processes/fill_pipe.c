/*
 * author: ablil
 * Description: Write random data to pipe until its filled
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

#define read 0
#define WRITE 1

int main(int argc, char const *argv[])
{
    int fd[2];
    pipe(fd);

    const char *buffer = "a";

    long double counter = 0;

    while ( 1 ) {
        counter++;
        int size = write(fd[WRITE], buffer, sizeof(char) * 61);
        printf("writtern %g bytes\n", counter);
        printf("size: %d\n", size);
    }
    return 0;
}
