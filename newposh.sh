#!/bin/bash

# if [ -z $1 ]; then
# 	c=`ls raw_pages/*.txt | wc -l`; cp raw_pages/${c}.txt raw_pages/$((${c}+1)).txt && rsub raw_pages/$((${c}+1)).txt
# else;

# echo 
if [ $1 == "c"]; then
	echo "a"	
else
	echo "b"	
fi




