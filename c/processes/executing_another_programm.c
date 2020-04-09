#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
		pid_t child = fork();

		if ( child == 0 ){
				execl("/bin/ls", "ls", "-a", "-l", NULL);
		} else {
				puts("waiting for another programm to finish");
				wait(NULL);
				printf("parent ps with pid %d\n", getpid());
		}
		return 0;
}

