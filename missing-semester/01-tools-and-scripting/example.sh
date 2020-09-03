#!/bin/bash

echo "Starting program at $(date)."
echo "Running program $0 with $# arguments."
echo "The program's PID is $$."

for file in "$@"; do
	grep 'signature' "$file" > /dev/null 2> /dev/null

	if [[ $? -ne 0 ]]; then
		echo "File $file does not have a signature. Adding one..."
		echo "# by mbalan" >> $file
	fi
done
