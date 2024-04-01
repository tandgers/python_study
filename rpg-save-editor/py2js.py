# python执行js (2)
import execjs
import os

dir2 = os.path.split(os.path.realpath(__file__))[0]
dir2 = dir2 + '\\t1.js'
text = execjs.compile(open(dir2).read())
input1 = '1'
input2 = {"globalId":"RPGMV","title":"花火链接","characters":[["Actor1",0]],"faces":[["A",0]],"playtime":"00:03:17","timestamp":1667062275778}

output = text.call('saveToLocalFile', 1, input2)
print(output)