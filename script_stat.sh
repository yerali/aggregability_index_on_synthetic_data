#!/bin/bash -e
                  
camino="/home/yerali/Dropbox/c/aggregation_synthetic/"

pr=0
nn=160
nn1=40
nn2=40
nn3=40
nn4=520
MIN=0.0
MAX=0.3
#DELTA=0.002
DELTA=0.01

rm stat.dat

CONTADOR=1
while [  $CONTADOR -lt 70 ]; do

   for p1 in $(seq $MIN $DELTA $MAX)
#for p1 in $(seq 0.5 0.001 0.6) 
#for p1 in 1 2 3 4 5
        do
#        echo $p1
	python2 creation_topology.py "$nn1" "$nn2" "$nn3" "$nn4"
	python2 rewiring.py "$p1"
	python2 community_detection.py "$p1" "$pr" >> stat.dat
        done

        let CONTADOR=CONTADOR+1 
        done

python2 average.py "$MIN" "$MAX" "$DELTA" > "eta_communes_heterog_stat.dat"   








