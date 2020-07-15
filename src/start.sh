#!bin/bash

cp /data/$1 ./$1
python main.py $1 $2
mkdir -p /data/output
cp *$1* /data/output
