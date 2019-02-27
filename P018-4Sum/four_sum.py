"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            for j in range(i+1, length):
                l = j + 1
                r = length -1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if target == total:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l<r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return res

nums = [1, 0, -1, 0, -2, 2]
nums = [0,0,0,0]
# nums = [-3,-2,-1,0,0,1,2,3]
# nums =[1,-2,-5,-4,-3,3,3,5]
print(Solution().fourSum(nums, 0))