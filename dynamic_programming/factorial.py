

# 递归，这个算法时间复杂度已经是O(n)了。
def fac(n):
    if n <= 1:
        return 1
    return n*fac(n-1)


# 这个时间复杂度和空间复杂度都是O(n)。
def fac2(n):
    result = [-1 for i in range(n+1)]
    def sub_func(n):
        if n <= 1:
            return 1
        if result[n] > 0:
            return result[n]
        result[n] = n*sub_func(n-1)
        return result[n]
    # 记住，返回的是子函数
    return sub_func(n)


print(fac(200))
print(fac2(200))