#!/bin/bash

echo '------'
echo 'ls -la'
ls -la

echo '------------'
echo 'READY TO RUN'
echo '------------'

echo ''
echo ' - start main - '
echo ''

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
LOGFILE="/home/photobox/projects/raspi-photo-box/logs/output_$TIMESTAMP.log"
mkdir -p /home/photobox/projects/raspi-photo-box/logs
sudo python3 -u main.py >> "$LOGFILE" 2>&1