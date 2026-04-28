### COIN-GAME-2

#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD identity &

# COMMUNICATION FAILURE
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.1 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.2 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.3 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.4 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.5 &
#wait
#if [ $? -ne 0 ]; then echo "A process failed"; fi

#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.6 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.7 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.8 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-UNSTABLE-COMMUNICATION identity 1.0 &
#wait
#if [ $? -ne 0 ]; then echo "A process failed"; fi

# MISRESPONDING
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.1 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.2 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.3 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.4 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.5 0.9 &
#wait
#if [ $? -ne 0 ]; then echo "A process failed"; fi

#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.6 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.7 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.8 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 0.9 0.9 &
#python  -m main.DRIVE_ext.train CoinGame-2 DRIVE-TD-RESPONSE-MISREPORTING identity 1.0 0.9 &
#wait
#if [ $? -ne 0 ]; then echo "A process failed"; fi

### COIN-GAME-4

python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD identity &

# COMMUNICATION FAILURE
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.1 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.2 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.3 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.4 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.5 &
wait
if [ $? -ne 0 ]; then echo "A process failed"; fi

python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.6 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.7 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.8 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-UNSTABLE-COMMUNICATION identity 1.0 &
wait
if [ $? -ne 0 ]; then echo "A process failed"; fi

# MISRESPONDING
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.1 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.2 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.3 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.4 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.5 0.9 &
wait
if [ $? -ne 0 ]; then echo "A process failed"; fi

python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.6 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.7 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.8 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 0.9 0.9 &
python  -m main.DRIVE_ext.train CoinGame-4 DRIVE-TD-RESPONSE-MISREPORTING identity 1.0 0.9 &
wait
if [ $? -ne 0 ]; then echo "A process failed"; fi