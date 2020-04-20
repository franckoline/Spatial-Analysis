# -*- coding: utf-8 -*-
"""
GDAL is an important library for GIS programming. Basically you can do very little in GIS without it as many of the key
libraries such as Fiona, Shapely and Pyproj depend on it. GDAL is written in C++ and is known to be tricky to install
and use with Python. Python and C/C++ generally play well together but, in my experience, GDAL is an exception to this.

This is only a problem if you are using MS Windows. Linux and Mac should be fine.
-----------------------------------------------------------------------------------------------------------

INSTRUCTIONS FOR MS WINDOWS USERS

I also recommend that you use Python 3.7 for the moment as I have tested the setup process with this version.
In the following examples I've given Win32 and AMD64 examples. Most modern computers will use the AMD64
version but if you get an error reporting an "unsupported wheel format" or similar, try the Win32 version.
It is almost impossible to predict in advance as computers vary widely.

To install GDAL download the file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal.
Choose GDAL‑3.0.4‑cp37‑cp37m‑win32.whl or GDAL‑3.0.4‑cp36‑cp36m‑win_amd64.whl.
To install Fiona download the file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona.
Choose Fiona‑1.8.13‑cp37‑cp37m‑win_amd64.whl or Fiona‑1.8.13‑cp37‑cp37m‑win32.whl.
To install Shapely download the file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely.
Choose Shapely‑1.6.4.post2‑cp37‑cp37m‑win_amd64.whl or Shapely‑1.6.4.post2‑cp37‑cp37m‑win32.whl.
To install Pyproj ddownload the file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj.
Choose pyproj‑2.4.2.post1‑cp37‑cp37m‑win32.whl or pyproj‑2.4.2.post1‑cp36‑cp36m‑win_amd64.whl.

For everything else, the standard pip install will be fine.

You should download this file to your project directory and import it as the first import in every GIS program that you
write. This will, hopefully, ensure a relatively painless experience when doing programming for GIS.

REMEMBER: THESE INSTRUCTIONS APPLY TO MS WINDOWS USERS ONLY.
-----------------------------------------------------------------------------------------------------------

INSTRUCTIONS FOR APPLE MAC AND LINUX USERS

If you are using Mac or Linux the process is simpler.

For MAC:
* Make sure that you have Homebrew installed. This is Apple's package manager for stuff other than that supplied by the
OS or from an App Store.
* From a TERMINAL window run: brew install gdal

For LINUX: Assumption is that your OS uses the APT package manager as is the case for Debian-based distributions such as
Ubuntu.
* From a TERMINAL window run: sudo apt-get install libgdal-dev

For Both MAC and LINUX
* Create your PyCharm project as usual.
* From PyCharm terminal run: pip install pygdal=="$(gdal-config --version).*"
* From PyCharm terminal run: pip install pyproj fiona shapely
-----------------------------------------------------------------------------------------------------------

Mark Foley
January 2019, updated January 2020
"""

import os
import distutils

if os.name == 'nt':
    # Only runs if os is MS Windows (coded as nt)
    from distutils.sysconfig import get_python_lib
    os.environ["PATH"] += os.pathsep + get_python_lib() + "\\osgeo"

    os.environ["PROJ_LIB"] = get_python_lib() + "\\osgeo\\data\\proj"
    os.environ["GDAL_DATA"] = get_python_lib() + "\\osgeo\\data\\gdal"

    # # Uncomment these lines if you need to inspect the contents of environment variables
    # for k,v in os.environ.items():
    #     print(f"{k}: {v}")
