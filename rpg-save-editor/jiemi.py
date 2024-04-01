# 将base64转换为str
from lzma import LZMACompressor, decompress
import lzstring
import json
import os

dir2 = os.path.split(os.path.realpath(__file__))[0]

f = open(dir2 + "\\original_jiami.txt")
data = f.read()
x = lzstring.LZString()

output = x.decompressFromBase64(data)
#将字典转换为字符串形式,并保存cookies
dir2 = os.path.split(os.path.realpath(__file__))[0]
with open(dir2+'\\RPG File1.json', 'w',newline='') as json_file:
    json.dump(output, json_file)
json_file.close()



