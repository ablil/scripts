#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>

int main() {

    unsigned long number = 1024;
    printf("Number: %d\n", number);
    printf("Number in hex: %0x\n", number);
    
    // dispaly in host endianess
    printf("Network endianess: %0x\n", ntohl(number));
    
    // display in network endianess
    printf("Network endianess: %0x\n", htonl(number));

    return 0;
}


