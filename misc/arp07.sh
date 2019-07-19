#!/bin/bash

# VERSION TO BE RUN
BUILD_VERSION='180719'

# Get the latest release and execute the application
cd ~
wget https://github.com/yenthusiastic/ARP07/archive/b${BUILD_VERSION}.zip
unzip ARP07-b${BUILD_VERSION}.zip
cd ARP07-b${BUILD_VERSION}
sudo python3 main.py
