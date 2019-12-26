#!/usr/bin/env python3
# updated : 01-14-2019

import os
import sys
import platform
from is_ipv4 import is_ipv4


def linux_changer(website, ip="0.0.0.0"):
    """
    append to /etc/hosts website with ip (default 0.0.0.0)
    """

    with open("/etc/hosts", "a+") as hosts:
        hosts.write("\n{}\t{}".format(ip, website))
    print("{} appended to hosts file SUCCESSFULLY.".format(website))

    # clear dns cache
    try:
        os.system("sudo /etc/init.d/nscd restart")
    except:
        # some linux dont have nscd installed on it
        print("clearing cache FAILED\napperently user dont have nscd")


def windows_changer(website, ip="0.0.0.0"):
    """
    append to c:/windows/system32/etc/hosts website with dns server (default 0.0.0.0)
    """

    os.chdir("C:/Windows/System32/drivers/etc")

    try:
        with open("hosts", "a+") as hosts:
            hosts.write("\n{}\t{}".format(ip, website))
        print("{} appended SUCCESSFULLY".format(website))
    except PermissionError:
        print("script should be run as ADMIN \naborting ...")
        exit()
    except Exception as e:
        raise e

    # clear dns cache
    os.system("ipconfig /flushdns")


if __name__ == "__main__":

    # system_env : {'Windows', 'Linux', 'Java'}
    # system_env : empty string if value cannot be determenied
    system_env = platform.system()
    website = None
    dns_server = None
    usage = "usage : python3 dns_changer.py facebook.com 127.0.0.1"

    if not len(system_env):
        print("CANNOT determine system platfrom !!!\nAborting ...")
        exit()

    # add help menu
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        print(usage)
        exit()

    # expect two args from user : website and dns server
    if len(sys.argv) in (2, 3):

        website = sys.argv[1]

        # check if dns server is passed & check if its valid
        try:
            dns_server = sys.argv[2]
            if not is_ipv4(sys.argv[2]):
                print("invalid dns server")
                print(usage)
                exit()
        except IndexError as e:
            # IndexError occured when dns server is not provided by user
            pass
        except Exception as e:
            # raise any other error for debugging purpose
            raise e
        finally:
            website = sys.argv[1]

        # perform actions based on system type
        if system_env == "Windows":
            windows_changer(website, dns_server)
        elif system_env == "Linux":
            linux_changer(website, dns_server)
        else:
            raise Exception("system is neither Windows nor Linux\nAborting...")
    else:
        print(usage)
