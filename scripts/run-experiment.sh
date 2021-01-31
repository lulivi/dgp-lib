#!/bin/bash

dataset="$1"

for i in {1..15}
do
   SEED="$(date +%s%N | cut -b14-19)"
   dgp -d "$dataset" -ip 64 -mg 32 -s $SEED
done
