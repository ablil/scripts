#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>

void signal_handler(int pid){
		printf("received a signal from ps: %d\n", pid);
}

int main(){
		pid_t child = fork();

		if ( child == 0 ){
				sleep(9);
				puts("child ps sending signal to parent ps");
				kill(getppid(), SIGHUP);
		} else {
				signal(SIGHUP, &signal_handler);
				pause();
				printf("parent ps with pid %d\n", getpid());
		}
		return 0;

}
