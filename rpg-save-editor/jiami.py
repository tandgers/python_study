# 将str转换为base64
from lzma import LZMACompressor, decompress
import lzstring
import json
import os


# 打开json文件
dir2 = os.path.split(os.path.realpath(__file__))[0]
with open(dir2+'\\RPG File1.json', 'r',newline='') as json_file:
    output = json.load(json_file)


# 保存为base64编码
x = lzstring.LZString()
output2 = x.compressToBase64(output)
with open(dir2+'\\chulihou_jiami.txt', 'w',newline='') as txt_file:
    txt_file.write(output2) 
txt_file.close()
