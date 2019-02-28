# 区间合并
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        length = len(intervals)
        if length < 2:
            return intervals
        intervals.sort(key = lambda x: x.start)
        res = []
        curr = intervals[0]
        for i in range(length):
            if curr.end >= intervals[i].start:
                curr = Interval(curr.start, max(curr.end, intervals[i].end))
            else:
                res.append(curr)
                curr = intervals[i]
        if i == (length - 1):
            res.append(curr)
        return res

    def merge2(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out

node1 = Interval(8,10)
node2 = Interval(1,3)
node3 = Interval(2,6)
node4 = Interval(15,18)
# li = [[8,10],[1,3],[2,6],[15,18]]
li = [node1, node2, node3, node4]
li = [Interval(1,4), Interval(4,5)]
res = Solution().merge(li)
print("99999999")
for i in range(len(res)):
    print(res[i].start, res[i].end)