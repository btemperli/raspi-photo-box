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

LOGFILE="/home/photobox/projects/raspi-photo-box/run.log"
sudo python3 main.py > "$LOGFILE" 2>&1