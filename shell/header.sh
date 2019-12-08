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
	echo "###########################################################" > "$script_name"
	echo -e "# Script Name\t: $script_name" >> "$script_name"
	echo -e "# Description\t:" >> "$script_name"
	echo -e "# Arguments\t: " >> "$script_name"
	echo -e "# Date\t\t: $creation_date" >> "$script_name"
	echo -e "# Author\t: $script_author" >> "$script_name"
	echo -e "# Email\t\t: $script_author_email" >> "$script_name"
	echo "###########################################################" >> "$script_name"
	
}

check_args
add_header
