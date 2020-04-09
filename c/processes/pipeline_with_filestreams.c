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

			FILE *inputStream = fdopen(fd[READ], "r");
			if ( inputStream == NULL )
					exit(EXIT_FAILURE);

			char *data = (char*)malloc(sizeof(char)*11);
			puts("reading data from pipeline ...");
			fgets(data, sizeof(data), inputStream);
			puts("closing pipeline ...");

			close(fd[READ]);
			fclose(inputStream);
			printf("Recieved: %s\n", data);
			free(data);

	} else {
			puts("closing pipe on read end ...");
			close(fd[READ]);

			sleep(3);
			FILE *outputStream = fdopen(fd[WRITE], "w");
			if ( outputStream == NULL )
					exit(EXIT_FAILURE);
			puts("sending data to pipeline ...");
			fprintf(outputStream, "Hello world");
			fflush(outputStream);
			puts("Finished: closiing pipeline ...");
			fclose(outputStream);
			close(fd[WRITE]);
			puts("==========================");

	}

	return 0;

}
