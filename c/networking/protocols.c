#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>

int main(int argc, char **argv) {

    int protocol_number = 4;
    char *protocol_name = "ipv6";
    struct protoent *protocol = malloc(sizeof(struct protoent));

    // get protocol by number example
    protocol = getprotobynumber(protocol_number);
    printf("Protocol number: %d\n", protocol->p_proto);
    printf("Protocol name: %s\n", protocol->p_name);

    // get protocol by name example
    protocol = getprotobyname(protocol_name);
    printf("Protocol number: %d\n", protocol->p_proto);
    printf("Protocol name: %s\n", protocol->p_name);

    // list all protocols from /etc/protocols
    setprotoent(0);
    while ( (protocol = getprotoent()) != NULL )
        printf("Protocol number: %d, protocol name; %s\n",
                protocol->p_proto, protocol->p_name);
    endprotoent();

    return 0;
}
