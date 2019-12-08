#!/usr/bin/bash
###########################################################
# Script Name	: queryXpath.sh
# Description	: run xpath queries from file with extension .xpath against .xml
# Arguments	: xpath file, xml file 
# Date		: 2019-11-10
# Author	: _ablil
# Email		: ablil@protonmail.com
# Note		: The script use the xpath option in xmllint, by default it is limited
# 		: to only run one string query
# 		: .xpath is meant to hold simple query line per line. 
###########################################################


####################### Global variable ##########################
xpathfile=$1
xmlfile=$2
#################################################################

function usage(){
	echo ""
	echo "Usage: $0 <xpath file> <xml file>"
	echo -e "\tExample: $0 queries.xpath myfile.xml"
}

function check_args(){

	# print Help 
	if [[ $xpathfile == "-h" ]]; then
		usage
		exit
	fi

	# check files existence
	if [[ ! -f $xpathfile ]]; then
		echo "Error: $xpathfile Not Found"
		exit
	fi
	if [[ ! -f $xmlfile ]]; then
		echo "Error: $xmlfile Not Found"
		exit
	fi

	# Check file extension .xpath & .xml
	if [[ ${xpathfile##*.} != "xpath" ]] || [[ ${xmlfile##*.} != "xml" ]]; then
		echo "Error: File Formats Are Invalid !!"
		usage
		exit
	fi

}

function query(){
	# run queries againt xml file
	i=1
	while IFS= read -r line; do
		echo ""
		echo -e "\e[91mQuery $i:\e[0m $line"
		xmllint --noout --xpath "$line" "$xmlfile"
		echo ""
	done < "$xpathfile"

}


check_args
query
