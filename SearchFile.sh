#!/bin/bash

if [ $# == 0 ];   then
    echo "Enter the directory path: "
    read directory

else
    command="$0"
    directory="$1"
    echo "file name: $command"
    echo "directory name: $directory"

fi

if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    exit 1
fi


find "$directory" -type f \( -name "*.c" -o -name "*.cpp" -o -name "*.py" \) | while read  file; do
    printf "%s: " "$file" 
    printf "%s lines, " "$(wc -l < "$file")"
    printf "%s characters and bytes\n" "$(wc -m < "$file")"

done


