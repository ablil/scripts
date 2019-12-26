#!/usr/bin/env python3
# updated : 15-01-2019

# using nmap is a better option.
# this script is too slow.
# it might be used under local network (meterpreter).

import argparse
import socket
from is_ipv4 import is_ipv4

# global variables
MIN_PORT = 1
MAX_PORT = 49150


def scan_host(host, port):
    """
    scan port on host & return True if open, False if closed.

    host : must be an ip address.
    port : must be a port number.
    """

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()

        return True
    except ConnectionRefusedError:
        return False
    except OSError:
        # some ports need permissions
        pass
    except TimeoutError:
        # port is likely closed when no response is received
        pass
    except Exception as e:
        print("port : {}".format(port))
        raise e


if __name__ == "__main__":

    target_ip = None
    port = None
    start_port, end_port = None, None  # port range
    status = False  # True if a port is opened

    # set up parsing args from command line process
    parser = argparse.ArgumentParser(description="python port scanner")
    parser.add_argument(
        "ip", metavar="target_ip", nargs=1, help="traget to scan (eg :127.43.180.42) "
    )

    args_group = parser.add_mutually_exclusive_group(required=True)
    args_group.add_argument(
        "-p",
        "--port",
        nargs=1,
        help="port to scan.\nseperate multiple port with comma. example :  -p 23,80,45 ",
    )
    args_group.add_argument(
        "-r",
        "--range",
        nargs=2,
        help="port range to scan, seperated by comma. eg : 80,100 ",
    )

    args = parser.parse_args()

    # read argument and setup variables and chech validity
    target_ip = args.ip[0]
    if not is_ipv4(target_ip):
        print("INVALID IP ADDRESS")
        exit()

    if args.port:
        try:
            port = int(args.port[0])
            assert port >= MIN_PORT and port < MAX_PORT
        except TypeError:
            print("INVALID PORT NUMBER")
        except AssertionError:
            print("valid ports number are between {} and {}".format(MIN_PORT, MAX_PORT))
        except Exception as e:
            raise e
    else:
        try:
            start_port, end_port = int(args.range[0]), int(args.range[1])
            assert MIN_PORT < start_port < end_port < MAX_PORT
        except ValueError:
            print("INVALID PORT NUMBER")
        except AssertionError:
            print("valid ports number are between {} and {}".format(MIN_PORT, MAX_PORT))
            print("check if {} < {}".format(start_port, end_port))

    if port:
        print("port {} : opened".format(port)) if scan_host(target_ip, port) else print(
            "port {} : closed".format(port)
        )
        exit()

    if start_port and end_port:
        print("scanning ports ...")

        for port in range(start_port, end_port + 1):
            if scan_host(target_ip, port):
                print("port {} : opened".format(port))
                status = True

        # display message for user if all ports are closed
        if not status:
            print("all ports in given range are closed !!!")

        exit()
