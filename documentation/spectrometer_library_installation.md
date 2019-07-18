### Installation Instructions 

* Clone the library from [HERE](https://github.com/ap--/python-seabreeze)

* Stuff you need for installing python-seabreeze without conda:
```bash
sudo apt-get install git-all build-essential libusb-dev
```

* Install the C library backend. Script is located in the misc folder:
```bash
./install_libseabreeze.sh
```

* Setup the udev rules. Theres another helper script in the misc folder:
```bash
./install_udev_rules.sh
```

* Install Cython to build cseabreeze:
```bash
pip install cython
```

* After that go to the repository root and run:
```bash
pip install .
```