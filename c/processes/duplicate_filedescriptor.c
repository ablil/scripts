#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(){

		int fd = open("testfile.txt", O_WRONLY | O_APPEND | O_CREAT);
		if ( fd == -1 ){
				perror("");
				exit(EXIT_FAILURE);
		}

		int dup_fd = dup(fd);
		if ( dup_fd == -1 ){
				perror("");
				exit(EXIT_FAILURE);
		}

		char *data = "this is a test os file descriptor duplication";
		int writtern = write(fd, data, strlen(data) / 2 );
		printf("I have written %d chars\n", writtern);

		if ( writtern == - 1){
				perror("");
		}
		close(dup_fd);
		close(fd);

		return 0;
}
