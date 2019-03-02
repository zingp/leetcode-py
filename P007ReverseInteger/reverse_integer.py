# 32位有符号整数反转
import math
class Solution:
    def reverse(self, x):
        sgin = 1
        if x < 0:
            sgin = -1
        res = 0
        x = abs(x)
        while x > 0:
            n = x % 10
            x //= 10
            res = res*10 + n
        res = sgin * res
        if res < -2**31 or res > (2**31-1):
            return 0
        return res