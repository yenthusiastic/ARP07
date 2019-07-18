######################################
# INSTALL OPENCV ON RASPBIAN STRETCH
######################################

# |          THIS SCRIPT IS TESTED CORRECTLY ON            |
# |--------------------------------------------------------|
# | OS                 | OpenCV       | Test | Last test   |
# |--------------------|--------------|------|-------------|
# | Raspbian 9 Stretch | OpenCV 4.1.0 | OK   | 12 Jul 2019 |


# IMPORTANT: Run following commands before executing the script
# Increase the SWAP on the Pi by changing CONF_SWAPSIZE in the file /etc/dphys-swapfile
# If you do not perform this step it’s very likely that your Pi will hang.
# sudo nano /etc/dphys-swapfile
# CONF_SWAPSIZE=2048           
# sudo /etc/init.d/dphys-swapfile stop
# sudo /etc/init.d/dphys-swapfile start


# VERSION TO BE INSTALLED

OPENCV_VERSION='4.1.0'


# 1. REMOVE UNNECESSARY PACKAGES AND KEEP OS UP TO DATE
sudo apt-get purge wolfram-engine   # Comment this line to keep Wolfram engine
sudo apt-get purge libreoffice*     # Comment this line to keep Libre Office
sudo apt-get clean
sudo apt-get -y autoremove          # Remove packages that are now no longer needed

sudo apt-get -y update
sudo apt-get -y upgrade             # Install the newest versions of all packages currently installed
# sudo apt-get -y dist-upgrade      # Uncomment this line to, in addition to 'upgrade', handles changing dependencies with new versions of packages
sudo apt-get -y autoremove          # Remove packages that are now no longer needed


# 2. INSTALL THE DEPENDENCIES

# Build tools:
sudo apt-get install -y build-essential cmake unzip pkg-config wget

# Media & Video I/O:
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev


# GUI backend 
sudo apt-get install -y libgtk-3-dev
sudo apt-get install -y libcanberra-gtk*   # Package to reduce GTK warnings

# Packages that contain numerical optimizations for OpenCV
sudo apt-get install -y libatlas-base-dev gfortran

# Python:
sudo apt-get install -y python3-dev

# Pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

# Numpy
sudo pip install numpy


# 3. INSTALL THE LIBRARY

cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip
unzip opencv.zip
unzip opencv_contrib.zip
rm opencv.zip
rm opencv_contrib.zip
mv opencv-${OPENCV_VERSION} opencv
mv opencv_contrib-${OPENCV_VERSION} opencv_contrib
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..
# Notice the -D OPENCV_ENABLE_NONFREE=ON  flag. Setting this flag with OpenCV 4 ensures that you’ll have access to SIFT/SURF and other patented algorithms.
# Be sure to update the above command to use the correct OPENCV_EXTRA_MODULES_PATH path if opencv and opencv_contrib folders are not both under home folder
make
sudo make install
sudo ldconfig

# Upon successful compilation, don't forget to go back to /etc/dphys-swapfile file and edit it:
#   - Reset CONF_SWAPSIZE to 100MB.
#   - Restart the swap service.

# 4. TEST OPENCV 4 INSTALLATION

# python3
# >>> import cv2
# >>> cv2.__version__
# '4.1.0'
# >>> exit()

