

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
#           空间换时间（注意分析时空复杂度）
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
