#/bin/env bash

n=0

std='std.out'
err='err.out'

while [[ $? == 0 ]]
do
	n=$(( n+1 ))
	./$1 > $std  2> $err
done

echo "Number of Successful runs: $(( n-1 ))"
echo "Failed on run #$n"
echo "`cat $std $err`"
