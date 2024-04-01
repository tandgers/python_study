#0823出行顺序
import random
from collections import Counter
out = []
random.seed('20230823') 
my_list = ['居住'] * 28 + ['工作/学习'] * 45 + ['途径路过'] * 20 + ['？？？'] * 20 
for i in range(0,80):
    out.append(random.choice(my_list))
print(out)
count = Counter(out)
print("列表中每个元素的个数为：", count)