#!/bin/sh
cd Reps_1.0.0/OtherComp
python Replicates.py &
cd ../Rep1
python Replicates.py &
cd ../Rep2
python Replicates.py &
cd ../Rep3
python Replicates.py &
cd ../../ 
rtresurrect -x Conn_4.xml
python main.py Conn_4.xml
