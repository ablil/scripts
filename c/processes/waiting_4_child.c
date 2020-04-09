#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
		pid_t child = fork();
		int wait_status;

		if ( child < 0 )
				puts("Cannot fork");
		else if ( child == 0 ){
				printf("child ps with pid: %d\n", getpid());
				// child ps doing long operations
				int i = 0;
				while ( i < 1000000000 )
						i++;
		} else {
				pid_t child = wait(&wait_status);
				printf("parent ps with pid: %d\n", getpid());
				printf("child ps has terminated execution\n");
				printf("wait status: %d\n", wait_status);
		}
		return 0;
}
