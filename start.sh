#!/bin/bash

# Define environment variables
HOST="0.0.0.0"
PORT=5000
PEERS="192.168.1.11,192.168.1.12"

# Export environment variables
echo "Exporting HOST=$HOST"
export HOST=$HOST
echo "Exporting PORT=$PORT"
export PORT=$PORT
echo "Exporting PEERS=$PEERS"
export PEERS=$PEERS

# Start application
echo "Starting application.... "
python src/app.py