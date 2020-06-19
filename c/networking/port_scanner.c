#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include <unistd.h>
#include <getopt.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <arpa/inet.h>

#define MIN_PORT 1
#define MAX_PORT 4000

extern char *optarg;
extern int optind, opterr, optopt;

void usage(char *filename);
int parse_args(int argc, char **argv, char *target, int *start_port, int *end_port);
int scan_port(int sock, char *target, int port);

int main(int argc, char **argv)
{

    char target[64];
    int start_port = 0;
    int end_port = 0;
    int port_status = 0;
    int flag = 0;
    int sock;

    flag = parse_args(argc, argv, target, &start_port, &end_port);

    fprintf(stdout, "[?] target: %s, start: %d, end: %d, status: %d\n",
            target, start_port, end_port, port_status);

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0)
    {
        fprintf(stderr, "[-] Failed to create socket\n");
        exit(EXIT_FAILURE);
    }

    if (flag > 0)
    {
        // scan only on port

        fprintf(stdout, "[*] Scanning port %d ...\n", start_port);
        port_status = scan_port(sock, target, start_port);

        if (port_status > 0)
            fprintf(stdout, "[+] Port %d is OPEN\n", start_port);
        else if (port_status < 0)
            fprintf(stdout, "[-] Port %d is CLOSED\n", start_port);
        else
            fprintf(stdout, "[?] Port state is UNKOWN\n");

        close(sock);
    }
    else if (flag < 0)
    {
        // scan a range of ports

        int open_ports = 0;

        fprintf(stdout, "[*] Scanning ...\n");

        for (int port = start_port; port <= end_port; port++)
        {
            if (scan_port(sock, target, port) > 0)
            {
                fprintf(stdout, "[+] Port %d is OPEN\n", start_port);
                open_ports++;
            }
        }

        fprintf(stdout, "[+] Total Number of OPEN Ports: %d\n", open_ports);
        close(sock);
    }
    else
    {
        fprintf(stderr, "[-] An Error Occured\n");
        return -1;
    }
    return 0;
}

void usage(char *filename)
{

    fprintf(stdout, "Port Scanner(TCP Only)\nUsage:\n");
    fprintf(stdout, "\t %s -t <target ip> -p <port>\n", filename);
    fprintf(stdout, "\t %s -t <target ip> -s <start port> -e <end port>\n", filename);
    exit(EXIT_FAILURE);
}

int parse_args(int argc, char **argv, char *target, int *start_port, int *end_port)
{

    int opt;
    int flags = 0;
    int port_flag = 0;
    int range_flag = 0;

    while ((opt = getopt(argc, argv, "t:p:s:e:")) != -1)
    {
        switch (opt)
        {
        case 't':
            flags++;
            strcpy(target, optarg);
            break;
        case 'p':
            flags++;
            port_flag = 1;
            *start_port = atoi(optarg);
            break;
        case 's':
            flags++;
            range_flag = 1;
            *start_port = atoi(optarg);
            break;
        case 'e':
            flags++;
            range_flag = 1;
            *end_port = atoi(optarg);
            break;
        default:
            break;
        }
    }

    if (flags != 2 && flags != 3)
        usage(argv[0]);

    if (port_flag && range_flag)
        usage(argv[0]);

    if (port_flag)
        return 1;

    if (range_flag)
        return -1;

    return 0;
}

int scan_port(int sock, char *target, int port)
{

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);

    if (inet_aton(target, &(addr.sin_addr)) == 0)
    {
        fprintf(stdout, "[-] Failed to create socket addr");
        fprintf(stdout, "[?] Reason: %s\n", strerror(errno));
        return 0;
    }

    if (connect(sock, (struct sockaddr *)&addr, sizeof(struct sockaddr)) != 0)
        return -1;
    else
        return 1;
}
