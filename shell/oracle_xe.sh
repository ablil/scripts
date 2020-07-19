#!/bin/bash
###########################################################
# Script Name	: oracle_xe.sh
# Description	: Install Orace Xe on Fedora (tested on Fedore 31)
# Arguments	:
# Date		: 2020-01-18
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################

oracle_package=$1

[[ $(id -u) != 0 ]] && { echo "Run as root"; exit 1; }

[[ -z "$1" ]] && {
	echo "Usage: ";
	echo -e "\tsudo bash $0 /path/to/oracle-database.rpm";
	exit 1;
}

# Check if oracle-database-xe*.rpm exists or not
[[ ! -f $oracle_package ]] && {
    
    echo "[-] $oracle_package NOT FOUND";
    echo "[?]Download from: https://www.oracle.com/database/technologies/xe-downloads.html"
    exit 1;
}

# Install dependencies

# install compat-libcap1
echo "[?] Downloading compat-libcap1-1.10-7.el7.i686.rpm ...";
curl http://mirror.centos.org/centos/7/os/x86_64/Packages/compat-libcap1-1.10-7.el7.i686.rpm --output compat-libcap1.rpm && {
    
    echo "[?] Installing compat-libcap1-1.10-7.el7.i686.rpm ...";
    dnf localinstall -y compat-libcap1.rpm || {
        echo "[-] Failed to install compat-libcpa1.rpm";
        exit 1;
    }
}


# install compat-libstdc++-33
echo "[?] Downloading compat-libstdc+ ...";
curl https://www.rpmfind.net/linux/fedora-secondary/releases/30/Everything/i386/os/Packages/c/compat-libstdc++-33-3.2.3-68.16.fc26.1.i686.rpm --output compat-libstdc.rpm && {
    
    echo "[?] Installing compat-libstdc+ ..."
    dnf localinstall -y compat-libstdc.rpm || {
        echo "[-] Failed to install compact-libstdc.rpm";
        exit 1;
    }
}



echo "[?] Downloading oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm ...";
curl -o oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm https://yum.oracle.com/repo/OracleLinux/OL7/latest/x86_64/getPackage/oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm && {
    
    echo "[?] Installing oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm ..."
    dnf localinstall -y oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm || {
        echo "Failed to install oracle-database-preinstall-18c-1.0-1.el7.x86_64.rpm";
        exit 1;
    }
    
    dnf localinstall -y "$oracle_package" || {
		echo "Failed to install $oracle_package"
	}
    
}


