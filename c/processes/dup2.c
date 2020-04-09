#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <signal.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>

#define READ 0
#define WRITE 1

int main(){

		puts("Executing the command ls -la | wc -l");

		int pipefd[2];
		if ( pipe(pipefd) == 1 ){
				perror("");
				exit(EXIT_FAILURE);
		}
		
		pid_t child = fork();
		if ( child == -1 ){
				perror("");
				exit(EXIT_FAILURE);
		} else if ( child == 0 ){
				close(pipefd[READ]);

				if ( dup2(pipefd[WRITE], STDOUT_FILENO) == -1 ){
						perror("");
						exit(EXIT_FAILURE);
				}
				close(pipefd[WRITE]);

				if ( execl("/usr/bin/ls", "ls", "-a", "-l", NULL) == -1 ){
						perror("");
						exit(EXIT_FAILURE);
				}
		} else {
				close(pipefd[WRITE]);

				if ( dup2(pipefd[READ], STDIN_FILENO) == -1 ){
						perror("");
						exit(EXIT_FAILURE);
				}

				close(pipefd[READ]);

				if ( execl("/usr/bin/wc", "wc", "-l", NULL) == -1 ){
						perror("");
						exit(EXIT_FAILURE);
				}

		}
		return 0;
}



