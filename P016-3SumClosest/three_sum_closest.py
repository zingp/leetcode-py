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
        print(nums)
        length = len(nums)
        if length < 3:
            return 
        for i in range(length):
            l = i+1
            r = length -1
            while l < r:
                print(i,l,r,"====",nums[i],nums[l], nums[r])
                total_sum = nums[i] + nums[l] + nums[r]
                print("total sum",total_sum,)
                diff = total_sum - target
                curr_diff = abs(diff)
                print("diff", curr_diff)
                if curr_diff == 0:
                    return total_sum
                if curr_diff < min_diff:
                    min_diff = curr_diff
                    print("----", curr_diff)
                    min_sum = total_sum
                if  l < r:
                    if diff < 0 and nums[i+1] < 0: 
                        r -= 1
                    elif diff < 0 and nums[i+1] >= 0: #[6]
                        l += 1
                    elif diff > 0 and nums[r-1] >0:
                        l += 1
                    else:
                        r -= 1
        return min_sum

# nums = [-1, 2, 1, -4]
nums = [0,2,1,-3]
print(Solution().threeSumClosest(nums, 1))
