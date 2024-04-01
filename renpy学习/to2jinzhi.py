import io
import zipfile
import os
import sys
import os

log = open('log',mode='rb+')
qian = log.read()
print(qian)
hou = open('log(chulihou2)',mode='w')
qian = str(qian)
hou.write(qian)
hou.close()