#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
		pid_t child = fork();

		if ( child == 0 ){
				puts("child is sleepinf for 5 seconds");
				sleep(5);
				printf("child ps with pid: %d\n", getpid());

		} else {
				printf("parent ps with pid: %d\n", getpid());
		}
		return 0;
}

