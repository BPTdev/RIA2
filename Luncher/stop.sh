#!/bin/bash

# Check if api_pid.txt exists and kill the process
if [ -f api_pid.txt ]; then
    kill -9 $(lsof -ti:5002)
    rm api_pid.txt
else
    echo "API server PID file not found."
fi

# Check if frontend_pid.txt exists and kill the process
if [ -f frontend_pid.txt ]; then
    kill -9 $(lsof -ti:5001)
    rm frontend_pid.txt
else
    echo "Frontend server PID file not found."
fi
