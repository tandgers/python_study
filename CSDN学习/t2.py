
# 请关闭中文输入法，用英文的字母和标点符号。
# 如果你想运行系统测试用例，请点击【执行代码】按钮，如果你想提交作答结果，请点击【提交】按钮，
# 注意：除答案外，请不要打印其他任何多余的字符，以免影响结果验证
# 本OJ系统是基于 OxCoder 技术开发，网址：www.oxcoder.com
# 模版代码提供基本的输入输出框架，可按个人代码习惯修改


class Solution:
    def __init__(self) -> None:
        pass
    
    def solution(self, n, k, l, c, d, p, nl, np):

        # TODO: 请在此编写代码
        
        for result in range(0,c*d+1):
            if result*n*nl > k*l or result*n > c*d or result*np*n > p:
                return result-1
                break
                    
                


if __name__ == "__main__":

    
    arr_temp = [int(item) for item in input().strip().split()]
    
    n = int(arr_temp[0])
    k = int(arr_temp[1])
    l = int(arr_temp[2])
    c = int(arr_temp[3])
    d = int(arr_temp[4])
    p = int(arr_temp[5])
    nl = int(arr_temp[6])
    np = int(arr_temp[7])


    sol = Solution()
    result = sol.solution(n, k, l, c, d, p, nl, np)
    print(result)
