#!bin/bash

cp /data/$1 ./$1
python main.py $1 $2
mkdir -p /data/output
cp *.* /data/output
rm /data/output/*.sh
rm /data/output/*.py
