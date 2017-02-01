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
rtresurrect -x Conn_4.xml
cd ../
python main.py rtc_replication_test/Conn_4.xml
