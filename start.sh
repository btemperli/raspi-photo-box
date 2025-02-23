#!/bin/bash

echo '------'
echo 'ls -la'
ls -la

echo '------'
echo 'whoami'
whoami

echo '------'
echo 'test'
echo "test output"


echo '------'
echo 'python --version'
python --version

echo '------'
echo 'pip install --upgrade pip'
pip install --upgrade pip

# install all apt's for openCV
#echo '------'
#echo 'sudo apt-get install openCV / cv2...'
#sudo apt-get update
#sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y
#sudo apt-get install python-opencv

echo '------'
echo 'pip install requirements.txt'
pip install opencv-python
pip install --no-cache-dir -r requirements.txt


echo '------------'
echo 'READY TO USE'
echo '------------'

echo ''
echo ''
echo ''
echo ' - start main - '
python main.py