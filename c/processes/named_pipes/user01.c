#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>

#define READ 0
#define WRITE 0

int main(){

		int create_pipe = mkfifo("named_pipe", 0666);
		if ( create_pipe == -1 ){
				perror("Named pipe creation");
		}

		char str1[80], str2[80];
		int fd;
		puts("Im user01");

		while ( 1 ){
				// first open for write only
				fd = open("named_pipe", O_WRONLY);

				printf("Type: ");
				fflush(stdin);
				scanf("%s", str1);

				write(fd, str1, strlen(str1)+1);

				close(fd);

				// then open for read only
				fd = open("named_pipe", O_RDONLY);
				
				read(fd, str2, sizeof(str2));

				close(fd);

				printf("User 02: %s\n", str2);
		}

		return 0;
}
