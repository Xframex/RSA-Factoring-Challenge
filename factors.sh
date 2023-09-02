#!/bin/bash

# Check for the correct number of arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: File '$input_file' does not exist."
    exit 1
fi

# Function to factorize a number into two smaller numbers
factorize() {
    n="$1"
    for ((i = 2; i <= n / 2; i++)); do
        if [ $((n % i)) -eq 0 ]; then
            echo "$n=$i*$((n / i))"
            return
        fi
    done
    echo "$n is prime"
}

# Process each line in the input file
while read -r line; do
    factorize "$line"
done < "$input_file"
