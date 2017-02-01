#!/bin/sh
cd OtherComp
python Replicates.py &
cd ../Rep1
python Replicates.py &
cd ../Rep2
python Replicates.py &
cd ../Rep3
python Replicates.py &
cd ../ 
rem rtresurrect -x test_replication.xml
rem cd ../
rem python main.py test_replication.xml
