#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
		pid_t child1 = fork();
		int wait_status;

		if ( child1 == 0 ) {
				printf("child 1 with pid: %d doing a long operation\n", getpid());
				int i = 0;
				while (i < 100000000)
						i++;
				puts("child 1 termniated");
				exit(1);
		}

		pid_t child2 = fork();
		if ( child2 == 0 ){
				printf("child 2 with pid: %d doing a long operation\n", getpid());
				int i = 0;
				while (i < 1000000000)
						i++;
				puts("child 2 termnated");
				exit(1);
		}

		printf("parent ps with pid: %d\n", getpid());
		printf("waiting only for ps with pid %d\n", child2);
		pid_t tmp = waitpid(child1, &wait_status, 0);
		printf("child 1 ps terminated\n");

		return 0;
}
