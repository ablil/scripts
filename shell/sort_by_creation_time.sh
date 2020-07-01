#!/bin/bash
###########################################################
# Script Name	: sort_by_creation_time.sh
# Description	: Sort files by creation time and not modification time
# Arguments	: Directory containing files/directories
# Date		: 2020-06-20
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################

[[ -z $1 ]] && echo -e "Usage:\t bash $0 <directory>" && exit;

format_ouput() {
# echo creation date followed by filename
    for file in $(find $1 -type f); do
        created_at=$(stat $file | tail -1 | cut -d ' ' -f3,4)
        filename=$file
        echo "$created_at $(basename $filename)"
    done;
}

format_ouput | sort
