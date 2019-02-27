"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        min_sum = (1<<31)-1
        min_diff = (1<<31)-1
        nums.sort()
        length = len(nums)
        if length < 3:
            return 
        for i in range(length):
            l = i+1
            r = length -1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(curr_sum - target) < min_diff:
                    min_diff = abs(curr_sum- target)
                    min_sum = curr_sum
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return min_sum

# nums = [-1, 2, 1, -4]
# nums = [0,2,1,-3]
nums = [1,1,-1,-1,3]
print(Solution().threeSumClosest(nums, -1))
