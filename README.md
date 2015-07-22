# Sky Wave Design, LLC
This is the Sky Wave Design, LLC template python application.

There is a setup script that will install all of the necessary packages in 
Ubuntu.  For now if you are in Windows or Mac you are on your own, but the code
will run on those environments with the proper setup.

## Ubuntu

1. `chmod +x python_setup.sh`
2. `sudo ./python_setup.sh`
3. `chmod +x mainwindow.py`
4. `./mainwindow.py`

## Windows [incomplete]

1. Download Python 3.4 64 bit for windows: https://www.python.org/ftp/python/3.4.3/python-3.4.3.amd64.msi
2. Install.  Make sure to select the option that adds the python install folder to the path
3. Open the command prompt
4. Run `pip install --update pip`
5. Download MSVC++ 10.0 x64 from here: http://download.microsoft.com/download/3/2/2/3224B87F-CFA0-4E70-BDA3-3DE650EFEBA5/vcredist_x64.exe
http://download.microsoft.com/download/5/B/C/5BC5DBB3-652D-4DCE-B14A-475AB85EEF6E/vcredist_x86.exe
## Mac OS X

Good luck!  This program requires python3 which means headaches for you!

With a bit of luck you can install homebrew, followed by python3, then use pip3
(not pip which is for python 2.7.x) to install the remaining packages
