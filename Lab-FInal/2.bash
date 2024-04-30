#!/bin/bash

directory="/mnt/e/Fourth-Semester/Systems-Programming/Lab-FInal/user_logs"

high=0
high_date=""
low=1000
low_date=""

for file in "$directory"/*; do
    filename=$(basename "$file")

    date="${filename#"log_"}"
    date="${date%.txt}"
    date="${date:6:2}-${date:4:2}-${date:0:4}"
    printf "$date\n"

    uniq_names_count=$(sort "$file" | uniq -c | wc -l)
    printf "$uniq_names_count\n"

    if [ "$uniq_names_count" -gt "$high" ]; then
        high="$uniq_names_count"
        high_date="$date"
    fi
    if [ "$uniq_names_count" -lt "$low" ]; then
        low="$uniq_names_count"
        low_date="$date"
    fi
done

printf "Highest unique names in date $high_date\n"
printf "Lowest unique names in date $low_date\n"


