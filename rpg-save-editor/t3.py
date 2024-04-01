# python执行js (1)
import execjs
import os
# from js_code import *

def js_from_file(file_name):
    """
    读取js文件
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result

# 编译加载js字符串
dir2 = os.path.split(os.path.realpath(__file__))[0]
dir2 = dir2 + '\\norm.js'
context1 = execjs.compile(js_from_file(dir2))

# 调用js代码中的add()方法，参数为2和3
# 方法名：add
# 参数：2和3
# 调用函数
print(context1.call('add', 1, 2))
# 获取变量名
print(context1.eval('t'))



