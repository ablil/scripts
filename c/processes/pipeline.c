#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

#define READ 0
#define WRITE 1


int main(){
	int fd[2];

	if ( pipe(fd) == -1){
			printf("could not create pipe\n");
			exit(EXIT_SUCCESS);
	}

	pid_t child = fork();
	if ( child == 0 ){
			puts("closing pipe on write end...");
			close(fd[WRITE]);

			char *data = (char*)malloc(sizeof(char)*11);
			puts("reading data to pipeline ...");
			read(fd[READ], data, 10);

			puts("closing pipeline ...");
			printf("Recieved: %s\n", data);

	} else {
			puts("closing pipe on read end ...");
			close(fd[READ]);

			
			puts("sending data to pipeline ...");
			char *data = "Hello world";
			write(fd[WRITE], data, 10);

			puts("Finished: closiing pipeline ...");
			close(fd[WRITE]);
	}

	return 0;

}
