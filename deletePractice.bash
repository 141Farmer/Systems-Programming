#!/bin/bash

$bin_dir=HOME/bin

if  [ ! -d "$bin_dir" ]; then
    mkdir "$bin_dir"
fi

remv()
{
    for file in "$@"; do
        mv "$file" "$bin_dir"
        printf " $file moved to recycle bin"
    done
}

restore()
{
    for file in "$@"; do
        if [ -e "$bin_dir"]; then
            mv "$bin_dir" 
            printf "Restored $file from recycle bin"
        else
            printf "FIle not found"
        fi
    done
}       
