#  寻找小和路径
"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

class Solution:
    
    def minimumTotal2(self, triangle):
        len_of_i = len(triangle)
        
        if len_of_i == 1:
            return triangle[0][0]
        
        for i in range(1, len_of_i):
            pre = triangle[i-1]
            cur = triangle[i]
            len_of_j = len(cur)
            for j in range(0, len_of_j):
                if j == 0:
                    cur[j] += pre[j]
                elif j == len_of_j - 1:
                    cur[j] += pre[-1]
                else:
                    cur[j] += min(pre[j-1], pre[j])
        
        return min(triangle[len_of_i-1])

inp = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
inp = [[-1],
      [2,3],
     [1,-1,-3]]

print(Solution().minimumTotal2(inp))