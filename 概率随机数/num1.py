#0823姓氏顺序
import random
from collections import Counter
out = []
random.seed('20230823') 
my_list = ['陈'] * 8484853 + ['黄'] * 5900718 + ['林'] * 5447168 + ['张'] * 3653621 + ['刘'] * 3158899 + ['梁'] * 2943083 + ['吴'] * 2754996 + ['杨'] * 2037085 + ['王'] * 1823554 + ['11-30'] * 20000000 + ['31-50'] * 15000000 + ['51-100/机动'] * 20000000
for i in range(0,80):
    out.append(random.choice(my_list))
print(out)
count = Counter(out)
print("列表中每个元素的个数为：", count)