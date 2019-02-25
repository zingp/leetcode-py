"""
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

主要思想是迭代nums中的每个数字。
我们使用数字作为目标来找到另外两个总数为零的数字。
对于其他两个数字，我们移动指针l和r来尝试它们。

l从左到右开始
r从右到左开始

首先，我们对数组进行排序，这样我们就可以轻松地移动我并知道如何调整l和r。
如果数字与之前的数字相同，我们已经将它用作目标，继续。 [1]
我们总是从i + 1开始左指针，因为组合已经尝试过。 [2]

现在我们计算总数
如果总数小于零，我们需要它更大，所以我们移动左指针。 [3]
如果总数大于零，我们需要它更小，所以我们移动右指针。 [4]
如果总数为零，找到了！ [5]
我们需要将左右指针移动到下一个不同的数字，所以我们不会得到重复的结果。 [6]

在nums [i]> 0之后我们不需要考虑i，因为正的总和将总是大于零。 [7]
我们不需要尝试最后两个，因为l和r指针没有空间。
你可以把它想象成最后两个已被其他所有人尝试过。 [8]
"""

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-1): #[8]
            if nums[i] > 0: 
                break  #[7]
            if i>0 and nums[i] == nums[i-1]: 
                continue   #[1]

            l, r = i+1, length-1 #[2]
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0: #[3]
                    l += 1
                elif total > 0: #[4]
                    r -= 1
                else:  #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]: #[6]
                        l += 1
                    while l<r and nums[r] == nums[r-1]: #[6]
                        r-=1
                    l += 1
                    r -= 1
        return res
        