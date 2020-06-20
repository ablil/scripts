#!/bin/bash
###########################################################
# Script Name	: backup_utility.sh
# Description	: backup and compresse a directory
# Arguments	: source directory (your want to make backup of), destination (backup dir)
# Date		: 2020-06-20
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################


usage() {
    echo "Usage: "
    echo -e "\tbash $0 <source directory> <backup directory>"
    exit
}
source=$1
destination=$2

# check arguments
([[ -z $source ]] || [[ -z $destination ]]) && usage;

# check permission and existence
[[ ! -d $source ]] && echo "Source directory does not exists" && exit;
[[ ! -d $destination ]] && echo "Destination directory does not exists" && exit;
[[ ! -d $destination ]] && echo "Write Permission is required on $destination" && exit;


# backup directory: Max depth 1
for directory in $(find $source -maxdepth 1 -type d); do
    backup_name="$destination/$(basename $directory)_backup.tar.gz";
    [[ $directory != $source ]] && tar cfz $backup_name $directory;
done

# back up file into one single archive file
tar cfz "$destination/$(basename $source)_backup.tar.gz" $(find $source -maxdepth 1 -type f);

