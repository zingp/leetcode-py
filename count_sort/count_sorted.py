
# 对10000个100 以内的整数排序， 可采用计数排序
def count_sort(li, max_num=100):
    tmp = [i for i in range(max_num+1)]
    for var in li:
        tmp[var] += 1
    li = []
    for index, count in enumerate(tmp):
        for j in range(count):
            li.append(index)
    return li

import random

li = [random.randint(0, 100) for _ in range(10000)]
li_sort= count_sort(li, max_num=100)
print(li_sort)
