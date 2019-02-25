"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i, dic[target - nums[i]]]
            else:
                dic[nums[i]] = i

    # 这个要快一点
    def twoSum2(self, nums, target):
        dic = {}
        for i, n in enumerate(nums):
            index = dic.get(target - nums[i], None)
            if index != None: 
                return [i, index]
            else:
                dic[n] = i
