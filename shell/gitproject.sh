#!/bin/bash
###########################################################
# Script Name	: gitproject.sh
# Description	: create and init new git repo, commit the frist commit
# Arguments	: directory name
# Date		: 2020-06-19
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################

function usage() {
    echo "gitproject";
    echo "$0 <directory_name>"
    echo -e "\tex: $0 mynewproject";
}

directory_name=$1

if [[ -z "$directory_name" ]]; then
    usage;
    exit -1;
else
    if [[ -d "$directory_name" ]]; then
        echo "Directory Already exists, choose another name";
        exit -1;
    else
        mkdir $directory_name;
        cd $directory_name;
        git init;
        echo `basename $directory_name` >> README.md;
        echo ".todo" >> .gitignore;
        git add .gitignore README.md
        git commit -m 'Initial commit';
        cd -
        echo "Finished";
    fi;
fi;
