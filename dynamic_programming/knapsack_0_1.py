# 0-1 背包问题


w = [2,2,6,5,4]
v = [3,6,5,4,6]
W = 10

# 暴力算法，两个边界条件
def search(idx, s):
    if s > W:
        return 0
    if idx == 0:
        return 0
    return max(search(idx - 1, s + w[idx]) + v[idx], search(idx - 1, s))

# 找冗余：构成s有很多种情况，同一大小的s被多次重复计算。

# 这个写出来有问题
print(search(len(w)-1, 0))