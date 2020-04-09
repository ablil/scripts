#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char** argv){
		puts("forking ps");

		pid_t child = fork();
		if ( child < 0 )
				puts("Cannot fork a child ps");
		else if ( child == 0 )
				printf("Child ps with pid: %d\n", getpid());
		else
				printf("Parent ps with id: %d\n", getpid());

		return 0;
		
}
