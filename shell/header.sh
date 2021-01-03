#!/bin/bash
# Author : _ablil
# Date: 2021-01-03
# Description: Add headers to scripts. 

creation_date=$(date +%Y-%m-%d)
author='ablil'

if [[ -z $1 ]]; then
	echo "create file with custom header"
	echo "Usage: ./$0 file"
	echo -e "\tExample: bash $0 server.py"
    exit 1;
else
    touch $1
    echo "" >> $1
    sed -i "1s/^/# Description: \\n/" $1
    sed -i "1s/^/# Date: $(date +%Y-%m-%d)\\n/" $1
    sed -i "1s/^/# Author: $author\\n/" $1
    sed -i "1s/^/#!\/usr\/bin\\n/" $1
fi
