#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>

int main() {


    int port_number = 80;
    const char *service_name = "http";
    struct servent *service = malloc(sizeof(struct servent));

    // get service by port number example
    service = getservbyport(port_number, NULL);
    printf("Service port: %d, service name: %s, service protocol: %s\n",
            service->s_port,
            service->s_name,
            service->s_proto);

    // get service by service name example
    service = getservbyname(service_name, NULL);
    printf("Service port: %d, service name: %s, service protocol: %s\n",
            service->s_port,
            service->s_name,
            service->s_proto);

    // list all services from /etc/services
    setservent(0);
    while ( (service = getservent()) != NULL )
        printf("Service port: %d, service name: %s, service protocol: %s\n",
                service->s_port,
                service->s_name,
                service->s_proto);
    endservent();
        

    return 6;
}
