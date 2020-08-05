#!/bin/bash
###########################################################
# Script Name	: backup.sh
# Description	: backup and compresse a directory into $backup_directory
# Arguments	: source directory (your want to make backup of), destination (backup dir)
# Date		: 2020-06-20
# Author	: _ablil
# Email		: ablil@protonmail.com
###########################################################

backup_directory=/backup
current_user=$(whoami)

usage() {
    echo "Backup and save file/directories into $backup_directory"
    echo ""
    echo "Usage: "
    echo -e "\tbash $0 dir1 dire2 dire3 file1 file2 ...."
    exit 1;
}


# check backup directory and permission
if [[ -d $backup_directory ]]; then
    if [[ ! -r $backup_directory ]] || [[ ! -w $backup_directory ]] || [[ ! -x $backup_directory ]]; then
        echo "You do not have permission on $backup_directory"
        exit 1;
    fi
else
    # create directory and give permission
    sudo mkdir -v $backup_directory
    sudo chown -R $current_user $backup_directory
fi


# backup files/directories
if [[ $# != 0 ]]; then
    echo "Backuping ..."

    for arg in $@; do

        # backup file
        if [[ -f $arg ]]; then
            filename=$arg
            timestamp=$(date +%Y%m%d_%H%M%S)
            cp -v -u $filename "${backup_directory}/${timestamp}_${filename}"

        # backup directory
        elif [[ -d $arg ]]; then
            directory=$arg
            archived=()

            echo "Archiving $directory ..."

            for item in $(ls $directory); do
                if [[ -d "$directory/$item" ]]; then
                    archive_name="$backup_directory/$item.tar"
                    
                    tar cf $archive_name "$directory/$item"
                    archived+=("$item.tar" )
                fi

                if [[ -f "$directory/$item" ]]; then
                    filename="$backup_directory/$item"
                    cp -v -u "$directory/$item" $filename
                    archived+=($item )
                fi

            done

            # archive all
            cd $backup_directory
            timestamp=$(date +%Y%m%d_%H%M%S)
            basename=$(basename $directory)
            archive_name="$backup_directory/${timestamp}_${basename}.tar"
            tar cf "$archive_name" "${archived[@]}" --remove-files
            cd -

        else
            echo "$arg DOES NOT EXIST"
        fi
    done
else
    usage
fi
