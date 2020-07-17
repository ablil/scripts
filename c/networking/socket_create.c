#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h> // memset() 
#include <unistd.h> // close()

int main() {

    // create socket
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    printf("socket file descriptor: %d\n", sock);

    // create bind address
    struct sockaddr_in *addr = malloc(sizeof(struct sockaddr_in));
    memset(addr, 0, sizeof(struct sockaddr_in));
    addr->sin_family = AF_INET;
    addr->sin_port = htonl(80);
    inet_aton("127.0.0.1", &(addr->sin_addr));

    // bind socket to addr
    int bind_status = bind(sock, 
                            (struct sockaddr*) addr,
                            sizeof(struct sockaddr_in));
    printf("bind status: %s\n",
            (bind_status == 0)? "sucess" : "fail");

    // close socket
    close(sock);

    return 0;
}
