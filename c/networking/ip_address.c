#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>

int main() {

    const char *ip = "172.153.19.34";
    struct in_addr *addr = malloc(sizeof(struct in_addr));
    struct in_addr *Ip = malloc(sizeof(struct in_addr));
    Ip->s_addr = 0x31314335;

    // tansfrom dotter ip notatation to network byteorder
    inet_aton(ip, addr);
    printf("ip: %s, net byteorder: %d\n",
            ip, addr->s_addr);

    // transform network byteorder to ip notation
    ip = inet_ntoa(*Ip);
    printf("ip: %s, net byteorder: %d\n",
            ip, Ip->s_addr);


    // get network address form ip
    Ip->s_addr = htonl(inet_netof(*addr));
    ip = inet_ntoa(*Ip);
    printf("Network ip: %s\n", ip);

    // get host address form ip
    Ip->s_addr = htonl(inet_lnaof(*addr));
    ip = inet_ntoa(*Ip);
    printf("Host ip: %s\n", ip);
    return 0;
}
