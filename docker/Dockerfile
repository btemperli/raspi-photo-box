FROM balenalib/raspberry-pi-debian-python:latest

WORKDIR /usr/src/app

COPY requirements.txt /

ADD start.sh /
RUN chmod +x /start.sh

#ECHO $HOME
#DATE

#RUN ["/bin/bash", "ls", "-la"]
#RUN ["/bin/echo", "hello World", "--no-cache"]

# RUN "ls" --no-cache
#RUN python --version --no-cache
#RUN echo "hello world" --no-cache
#RUN pip install --no-cache-dir -r requirements.txt

RUN sudo apt-get update
RUN sudo apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    libjpeg-dev \
    libtiff5-dev \
    libjasper-dev \
    libpng-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libfontconfig1-dev \
    libcairo2-dev \
    libgdk-pixbuf2.0-dev \
    libpango1.0-dev \
    libgtk2.0-dev \
    libgtk-3-dev \
    libatlas-base-dev \
    gfortran \
    libhdf5-dev \
    libhdf5-serial-dev \
    libhdf5-103 \
    python3-pyqt5 \
    python3-dev

RUN sudo apt-get install -y \
    python3-opencv

COPY .. .

#CMD ["python", "./main.py"]

CMD ["/start.sh"]
