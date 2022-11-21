#!/bin/bash

now=`date +%Y-%m-%d-%H%M%S` 

git diff --name-only | xargs tar -czf ${now}.tar.gz

echo "backed up ${now}.tar.gz"
echo "extrac command, tar -xzvf ${now}.tar.gz"