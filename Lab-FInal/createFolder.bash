#!/bin/bash

rm -r user_logs
mkdir -p user_logs

filename="user_logs/log_20240430.txt"
echo "ab" >> "$filename"
echo "ab" >> "$filename"
echo "ab" >> "$filename"

filename="user_logs/log_20240530.txt"
echo "ab" >> "$filename"
echo "bc" >> "$filename"
echo "cd" >> "$filename"

filename="user_logs/log_20240630.txt"
echo "bc" >> "$filename"
echo "ab" >> "$filename"
echo "ab" >> "$filename"

printf "done\n"