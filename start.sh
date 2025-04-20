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
sudo pip3 install opencv-python
sudo pip3 install events
sudo pip3 install pygame
sudo pip3 install python-dotenv

echo '------------'
echo 'READY TO USE'
echo '------------'

echo ''
echo ''
echo ''
echo ' - start main - '
sudo python3 main.py