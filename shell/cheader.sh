#!/bin/bash

#############################################################################
# Script Name	: header.sh
# Description	: Add headers to scripts. 
# Args:		: script name 
# Author	: _ablil
# Email		: ablil@protonmail.com
# Note		: If script doesnt exists, the script will prompt the user to create new one
#############################################################################

############ Global varaible to change #########################
script_name=$1
creation_date=$(date +%Y-%m-%d)
script_author='_ablil'
script_author_email='ablil@protonmail.com'
#################################################################

function usage(){
	echo ""
	echo "Add headers to scripts"
	echo "Usage: ./$0 script_name"
	echo -e "\tExample: bash $0 server.py"
	echo ""
}

function check_args(){
	# print usage if no args is passed 
	if [[ -z $script_name ]]; then
		usage
		exit 1234
	fi

	# check script existence
	if [[ ! -e "$script_name" ]] || [[ ! -f "$script_name" ]]; then
		echo "Warning: $script_name does NOT exist !!!"
		echo "Do you want to create [y/n]: "
		read -r choice
		if [[ "$choice" == 'y' ]] || [[ "$choice" == 'Y' ]]; then
			touch $script_name
			echo "$script_name is created"
		elif [[ "$choice" == 'n' ]] || [[ "$choice" == 'N' ]]; then
			exit
		else 
			echo "Invalid Input !!"
			exit 1
		fi
	fi
}


function add_header(){
	echo "#include <stdio.h>" > "$script_name"
	echo "#include <stdlib.h>" >> "$script_name"
	echo "#include <sys/types.h>">> "$script_name"
	echo "#include <unistd.h>" >> "$script_name"
	echo "#include <signal.h>" >> "$script_name"
	echo "#include <stdio.h>" >> "$script_name"
	echo "#include <sys/types.h>" >> "$script_name"
	echo "#include <sys/socket.h>" >> "$script_name"
	echo "#include <unistd.h>" >> "$script_name"
	echo "#include <netinet/in.h>" >> "$script_name"
	echo "#include <arpa/inet.h>" >> "$script_name"
	echo "#include <netdb.h>" >> "$script_name"
	echo "#include <unistd.h>" >> "$script_name"
	echo "#include <signal.h>" >> "$script_name"
	echo "#include <stdio.h>" >> "$script_name"
	echo "#include <string.h>" >> "$script_name"
	echo "#include <fcntl.h>" >> "$script_name"
	echo "#include <errno.h>" >> "$script_name"
	echo "#include <sys/time.h>" >> "$script_name"
	echo "#include <stdlib.h>" >> "$script_name"
	echo "#include <memory.h>" >> "$script_name"
	echo "#include <ifaddrs.h>" >> "$script_name"
	echo "#include <net/if.h>" >> "$script_name"
	echo "#include <stdarg.h>" >> "$script_name"
	echo "#include <math.h>" >> "$script_name"
	echo "#include <sys/types.h>" >> "$script_name"
	echo "#include <sys/socket.h>" >> "$script_name"


}

check_args
add_header
