#!/bin/bash

echo '------'
echo 'ls -la'
ls -la

echo '------'
echo 'whoami'
whoami

echo '------'
echo 'python3 --version'
python3 --version

echo '------'
echo 'pip install --upgrade pip'
pip install --upgrade pip

echo '------'
echo 'pip install the required libraries'
pip install opencv-python
pip install events
pip install pygame

echo '------------'
echo 'READY TO USE'
echo '------------'

echo ''
echo ''
echo ''
echo ' - start main - '
sudo python3 main.py