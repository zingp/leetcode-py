"""
Given a set of distinct integers（不同的整数）, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
import itertools

class Solution:
    def subsets(self, nums):
        res = []
        def sub(bits):
            if len(bits) == len(nums):
                res.append(list(itertools.compress(nums, bits)))
                return
            sub(bits+[True])
            sub(bits+[False])
        sub([])
        return res

a = list(itertools.compress([1,2,3,4], [0,1,4,5]))
li = [1,2,3]

print(Solution().subsets(li))