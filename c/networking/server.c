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

#define exit exit(EXIT_FAILURE);

int main (int argc, char ** argv) {

	// create socket
	int sock;
	if ( (sock = socket(AF_INET, SOCK_STREAM, 0)) < 0 ) {
		perror("error creating socket"); 
		exit;
	}

	// create sockeaddr
	struct sockaddr_in addr;
	memset(&addr, 0, sizeof(struct sockaddr));
	addr.sin_family = AF_INET;
	addr.sin_port = htons(1337);
	inet_aton("127.0.0.1", &(addr.sin_addr));
	
	// bind addr
	if ( (bind(sock, (struct sockaddr*)&addr, sizeof(struct sockaddr_in)) < 0 )) {
		perror("error binding");
		exit;
	}
	fprintf(stdout, "Binding ...");

	// get addresse of biund socket
	struct sockaddr_in bound_addr;
	socklen_t *lenght = malloc(sizeof(socklen_t));
	*lenght = sizeof(struct sockaddr_in);
	if ( getsockname(sock, (struct sockaddr*) &bound_addr, lenght) != 0 ) {
		perror("getting sockname error");
		exit;
	}
	fprintf(stdout, "addr: %s\n", inet_ntoa(bound_addr.sin_addr));

	// listening for connection 
	if ( listen(sock, 3) != 0 ) {
		perror("Error listening");
		exit;
	}

	// accepting connection
	int new_sock;
	if ( (new_sock = accept(sock, (struct sockaddr*) &addr, lenght)) < 0 ) {
		perror("error accepting connection ...");
		exit;
	} else {
		fprintf(stdout, "accepted connnection\n");
		char *msg = "Hello from server";
		char *buff = malloc(1024);
		ssize_t data = read(new_sock, (void*) buff, 1024);
		fprintf(stdout, "Recived: %s\n", buff);
		
		send(new_sock, (void*) msg, strlen(msg), 0);
		close(new_sock);
	}

	fprintf(stdout, "listening ...\n");
	fprintf(stdout, "Finished\n");
	close(sock);
	return 0;
}	
