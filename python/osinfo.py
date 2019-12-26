#!/usr/bin/env python3

import platform
import os
import time

if __name__ == "__main__":

    # os info
    arch = "arch : " + platform.machine()
    node_name = "node name : " + platform.node()
    processor = "processor : " + platform.processor()
    os_name = platform.system()
    os_release = "os release : " + platform.release()
    os_version = "os version: " + platform.version()
    current_time = "local time : " + time.asctime()

    # windows specific :
    os_servicepack = None
    path_win = None
    user_win = None
    if os_name == "Windows":
        os_servicepack = "service pack : " + platform.win32_ver()[2]
        path_win = "path : " + os.environ["PATH"]
        user_win = "user : " + os.environ["USERNAME"]

    # linux specific :
    dist_name = None
    dist_version = None
    user_linux = None
    path_unix = None
    lang = None
    user_id = None
    if os_name == "Linux":
        dist_name = "dist name : " + platform.dist()[0]
        dist_version = "dist version: " + platform.dist()[1]
        user = "user : " + os.environ["USER"]
        path_unix = "path : " + os.environ["PATH"]
        lang = "lang : " + os.environ["LANG"]
        user_id = (
            "user id : "
            + str(os.getresuid()[0])
            + " "
            + str(os.getresuid()[1])
            + " "
            + str(os.getresuid()[0])
        )

    # python info
    build = (
        "python build : "
        + platform.python_build()[0]
        + " "
        + platform.python_build()[1]
    )
    version = "python version : " + platform.python_version()
    compiler = "python compiler : " + platform.python_compiler()

    # display information to screen
    print(arch)
    print(node_name)
    print(processor)
    print("os name : {}".format(os_name))
    print(os_release)
    print(os_version)
    print(current_time)
    if os_name == "Windows":
        print(os_servicepack)
        print(path_win)
        print(user_win)
    if os_name == "linux":
        print(dist_name)
        print(dist_version)
        print(user)
        print(path_unix)
        print(lang)
        print(user_id)
    print(build)
    print(version)
    print(compiler)
