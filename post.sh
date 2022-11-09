#!/bin/bash

if [ -z "$1" ]; then
  c=`ls raw_pages/*.txt | wc -l`; cp raw_pages/${c}.txt raw_pages/$((${c}+1)).txt && rsub raw_pages/$((${c}+1)).txt
else
  git config user.name "chulwook.jeon"
  cd raw_pages && python convert.py && cd ..;git add --all && git commit -m "added" && git push origin main
fi