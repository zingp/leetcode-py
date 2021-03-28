# 动态规划的本质就是递归

# 暴力搜索 时间复杂度O(2^n）
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.solve(len(nums)-1, nums)

    def solve(self, index, nums):
        if index < 0:
            return 0
        return max(nums[index]+self.solve(index-2, nums), self.solve(index-1, nums))

test_num = [1, 2, 1, 4]

obj = Solution()
res = obj.rob(test_num)
print(res)

# 这样会存在问题
# 假设第一次抢的是第n-1家店，下次可以抢n-3,n-4...
# 假设第一次抢的是第n-2家店，下次可以抢n-4,n-5...
# 其实n-4之后都差不多，就会造成大量重复计算

# 最优子结构：子问题的的最优结果可以导出原问题的最优结果
#           无后效性
# 重叠子问题：
#           去冗余
#           空间换时间（注意分析时空复杂度）比如开一个列表，存储算过的
# 凡是决策都有可能有后效性，

# 40分钟

'''
def solve(self, index, nums):
        if index 算过：
            return 结果
        # 边界条件就是小于0
        if index < 0:
            return 0
        return max(nums[index]+self.solve(index-2, nums), self.solve(index-1, nums))
'''

# 计划搜索（备忘录），每次搜索后的数据都写在一个数组中记录了。遍历一遍，只计算一次。
class Solution2:
    def __init__(self):
        self.result = []

    def solve(self, index, nums):
        if index < 0:
            return 0
        if self.result[index] >=0:
            return self.result[index]
        self.result[index] = max(nums[index]+self.solve(index-2, nums), self.solve(index-1, nums))
        return self.result[index]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.result = [-1 for i in range(len(nums))]
        return self.solve(len(nums)-1, nums)

obj = Solution2()
res = obj.rob(test_num)
print(res)

# 一些有意思的解答
def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    f1=f2=0
    for i in range(len(nums)):
        f1,f2 = max(f1,f2+nums[i]),f1
    return f1

class Solution3:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0	
        if n == 1:
            return nums[0]
            
        res = [0  for i in range(n)]

        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i-1], nums[i] + res[i-2])
            # either add a number or its neighbour depending which gives maximum sum

        return res[n-1]

# 动态规划的题基本有以下特点：
# 最优最大最长最小
# 离散的，一般连续的问题不能用动态规划，因为要开一个数组，数组的下标是整数，不是小数
# 最优子结构

# 解题思路：
# 先设计一个暴力算法，找到冗余
# 设计并存储状态（一维二维三维数组， 甚至map）
# 递归式（状态转移方程）
# 自底向上计算最优解（编程方式）

# 递归改成非递归-->递推