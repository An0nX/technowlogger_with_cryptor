import os
import subprocess as sbp
import time
from base64 import b64decode as b64d
time.sleep(1)
temp = sbp.check_output("cmd /c echo %temp%").decode().replace("\r\n","")
b64data = b'WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo='
with open(f"{temp}\\INST.exe","wb")as f:
    f.write(b64d(b64data))
os.system(f"{temp}\\INST.exe")