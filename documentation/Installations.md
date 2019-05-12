### Instructions for installing required softwares
*All installations are done on Windows 10 unless otherwise specified*
#### Installing Python 3.5
Download and install [Python 3.5](https://www.python.org/downloads/windows/) (tested working with v3.5.3)
#### Installing PyQt for GUI app development
##### Option 1: Install from executable
- Download the PyQt5-5.6-gpl-Py3.5-Qt5.6.0-x64-2.exe from [this link](https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.6/) and execute it to install QtDesigner.
- Launch QtDesigner from Start Menu.
##### Option 2: Install using `pip` Python package manager
- In Commmand Line, type in:
```bash
pip install PyQt5
pip install pyqt5-tools
```
- To launch QtDesigner, go to `C:\Users\***\AppData\Local\Programs\Python\Python35\Lib\site-packages\pyqt5_tools` and launch `designer.exe` 
*(replace `***` with corresponding username on Windows)*

A comprehensive guide to PyQT can be found [here](https://www.pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/).
