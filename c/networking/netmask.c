/*
 * Author: ablil
 * Get net/host addr from ip using & operator
 */

#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main (int argc, char **argv) {

	if ( argc <= 1 ){
		fprintf(stdout, "usage: ./%s 127.0.0.1 192.168.1.5 ...\n", argv[0]);
	} else {
		struct in_addr addr;
		struct in_addr net;
		struct in_addr local;

		for (int i = 1; i < argc; i++) {
			inet_aton(argv[i], &addr);
			if ( addr.s_addr < htonl(0x80000000L) ) {
				puts("class A");
				net.s_addr = addr.s_addr & htonl(0xff000000L);
				local.s_addr = addr.s_addr & htonl(0x00ffffffL);
			} else if ( addr.s_addr < htonl(0xc0000000L) ) {
				puts("class B");
				net.s_addr = addr.s_addr & htonl(0xffff0000L);			
				local.s_addr = addr.s_addr & htonl(0x0000ffffL);
			} else {
				puts("class C");
				net.s_addr = addr.s_addr & htonl(0xffffff00L);
				local.s_addr = addr.s_addr & htonl(0x000000ffL);
			}


			fprintf(stdout, "Network: %s\n", inet_ntoa(net));
			fprintf(stdout, "Host: %s\n", inet_ntoa(local));
		}
	}
	return 0;
}
