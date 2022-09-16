import os
import sys
try:
    import rich
except ImportError:
    os.system('pip install rich')
try:
    import requests
except ImportError:
    os.system('pip install reqeusts')
try:
    import bs4
except ImportError:
    os.system('pip install bs4')
try:
    import stdiomask
except ImportError:
    os.system('pip install stdiomask')

try:
    import requests
    sys.clear()
    print("1000000000% DOOOONE \n BY ZEYAD ALABANY")
except ImportError:
    sys.clear()
    print("\033[1;31m ERROR MYABE YOUR TERMUX CRASH DOWNLOAD ORGINALA TERMUX FROM HERE")
    os.system('xdg-open https://f-droid.org/repo/com.termux_118.apk')
