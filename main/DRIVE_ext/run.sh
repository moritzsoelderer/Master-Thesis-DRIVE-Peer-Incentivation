export PYTHONPATH=$PYTHONPATH:.


python  lib/philippaltmann/DRIVE/train.py CoinGame-2 DRIVE-TD identity &
python  lib/philippaltmann/DRIVE/train.py CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity &
python  lib/philippaltmann/DRIVE/train.py CoinGame-4 DRIVE-TD identity &
python  lib/philippaltmann/DRIVE/train.py CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity &
python  lib/philippaltmann/DRIVE/train.py Harvest-12 DRIVE-TD identity &
python  lib/philippaltmann/DRIVE/train.py Harvest-12 DRIVE-TD-UNSTABLE-COMMUNICATION identity &
wait