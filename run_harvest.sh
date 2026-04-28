python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD identity &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.1 &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.2 &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.3 &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.4 &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.5 &
wait
if [ $? -ne 0 ]; then echo "A process failed"; fi

python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.6 &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.7 &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.8 &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.9 &
python  -m main.DRIVE_ext.train Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity 1.0 &
wait
if [ $? -ne 0 ]; then echo "A process failed"; fi