#!bin/bash

cp /data/$1 ./$1
python phylogenetic.py $1 $2
mkdir -p /data/output
cp *.treefile /data/output
cp *.log /data/output
