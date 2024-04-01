def jisuan(A):
    #shuru = input("input 常数C= ")
    #C = int(shuru)
    # 初始值
    # A = 61235275               # 游戏显示值
    # B = 1704649568      # 内存中的值，也是CE中搜索的值
    # C = 4253557641      # 常数

    ans1 = A*16384

    if(ans1 > 4294967295):
            # ans1大于FFFFFFFF(16进制)，产生溢出
        ans1_16jin = '{:x}'.format(ans1)
        ans1_1 = ans1>>32                       # 溢出的高位（10进制）
        ans2 = ans1_1<<32                       
        ans1_2 = '{:x}'.format(ans1_1)          # 溢出的高位（16进制）
        ans3 = ans1 - ans2                      # 得到低位（10进制）
        weiyihou = ans1_1 + ans3
        anss = '{:x}'.format(weiyihou) 
    else:
        weiyihou = ans1
    B = weiyihou ^ C
    C1 = C

    print("B = ",B)


shuru = input("请输入 常数C= ")
C = int(shuru)

while 1==1:
    shuru = input("请输入 游戏内显示的数值 A= ")
    A = int(shuru)
    jisuan(A)
