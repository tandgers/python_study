import io
import os
import sys
import time
import pickle

class Email():
    email = "tandgers@gmail.com"
s = open("G:/python学习专用/2023/renpy学习/1-1-LT1(after1)/log(after).log",mode = 'rb+')
out = s.read()
# out.decode("latin-1")
# s1 = io.BytesIO(out)
out0 = pickle.loads(out)

# out2 = renpy.pickle.Unpickler(s,fix_imports=True, encoding="utf-8", errors="surrogateescape")
# out3 = pickle.load(s)


text = 'helloworld'

sertext = pickle.dumps(text)
# print(sertext)
reltext = pickle.loads(sertext)
print(reltext)
 
# pickle.loads() #对象反序列化
# pickle.load() #对象反序列化，从文件中读取数据



# out1 = io.BytesIO(out)
#
time.sleep(3)

time.sleep(3)