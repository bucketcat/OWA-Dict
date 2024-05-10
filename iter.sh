#!/bin/bash

# Define the path to the list of domains
DOMAIN_LIST="domain_list.txt"

# Define the path to the wordlist for gobuster
WORDLIST="/path/to/wordlist.txt"

# Define the directory where you want to save the output files
OUTPUT_DIR="/path/to/output/"

# Iterate through each domain in the domain list
while IFS= read -r domain; do
    # Define the output file name based on the domain
    output_file="${OUTPUT_DIR}gobuster_output_${domain//./_}.txt"

    # Run gobuster for DNS enumeration
    gobuster dns -d "$domain" -w "$WORDLIST" -o "$output_file"

    # Run gobuster for vhost enumeration
    gobuster vhost -u "http://$domain" -w "$WORDLIST" -o "$output_file"
done < "$DOMAIN_LIST"
