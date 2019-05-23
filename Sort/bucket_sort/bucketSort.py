
# 桶排序 同排序的时间复杂度O(n+k) O(n^2 *k)和空间复杂度O(nk)
# 假设有10000个0-10000内的数排序
def bucket_sort(array, n=100,  max_num=10000):
    tmpl = [[] for _ in range(n)]
    for i in array:
        index = min(i // (10000//n), n-1)
        tmpl[index].append(i)
        for j in range(len(tmpl[index])-1, 1, -1):
            if tmpl[index][j] < tmpl[index][j-1]:
                tmpl[index][j],  tmpl[index][j-1] =  tmpl[index][j-1], tmpl[index][j]
            else:
                break
    li = [] 
    for sublist in enumerate(tmpl):
        for num in sublist:
            li.append(num)
    return li

import random
li = [random.randint(0,10000) for _ in range(10000)]
re_li = bucket_sort(li)
print(re_li)