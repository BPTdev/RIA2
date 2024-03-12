#!/bin/bash

# Start frontend.sh as a background process and save its PID
./frontend.sh &
echo $! > frontend_pid.txt

# Start api.sh as a background process and save its PID
# ./api.sh &
# echo $! > api_pid.txt

