#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/time.h>
#include <stdlib.h>
#include <memory.h>
#include <ifaddrs.h>
#include <net/if.h>
#include <stdarg.h>
#include <math.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <string.h>

int main (int argc, char **argv) {

	// create socket
	int sock;
	if ( (sock = socket(AF_INET, SOCK_STREAM, 0) ) < 0 ) {
		perror("Error creating socket");
		return -1;
	}
	
	// create addr struct
	struct sockaddr_in *addr = malloc(sizeof(struct sockaddr_in));
	addr->sin_family = AF_INET;
	addr->sin_port = htons(1337);
	if ( inet_aton("127.0.0.1", &(addr->sin_addr)) == 0 ) {
		perror("Error creaing addr ");
		return -1;
	}

	// connect to server
	if ( connect(sock, (struct sockaddr*) addr, sizeof(struct sockaddr_in)) != 0 ) {
		perror("Coould not connec to host machine");
		return -1;
	} else {
		char *msg = "Hello from client";
		char *buff = malloc(1024);

		send(sock, (void*) msg, strlen(msg), 0);
		ssize_t data = read(sock, (void*) buff, 1024);
		fprintf(stdout, "recieved: %s\n", buff);
	}
	close(sock);
		

	return 0;
}
