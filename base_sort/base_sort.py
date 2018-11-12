import math
import random


# 基数排序的平均时间复杂度是o(kn),其中k是最大数的位数
def based_sort(array):
    max_num = max(array)
    w = int(math.log10(max_num)+1)
    for i in range(w):
        buckets = [[] for _ in range(10)]
        for j in array:
            index = (j // (10**i)) % 10
            buckets[index].append(j)
        array.clear()   # 清空列表
        # 重新写入
        for buck in buckets:
            array.extend(buck)


# 基数排序的基本思想：
# 分为0-9  10个桶
# 从个位开始放入通
# li.clear()

# 基数排序很快
li = list(range(100000))
random.shuffle(li)
based_sort(li)
print(li)
