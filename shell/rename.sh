#!/bin/bash

function usage() {
    echo "Description:"
    echo -e "\tprefix the filename with current timestamp"
    echo "usage: "
    echo -e "\tbash $0 file"
    exit 1;
}

function rename_file() {
    old_filename=$1
    basename=$(basename $old_filename)
    dirname=$(dirname $old_filename)
    timestamp=$(date +%Y%m%d%H%M%S)

    mv "$old_filename" "$dirname/$timestamp-$basename"
}


[[ -z $1 ]] && usage
rename_file $1


