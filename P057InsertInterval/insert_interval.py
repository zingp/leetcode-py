"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
给定一组非重叠区间，在区间中插入新区间（必要时合并）。
您可以假设区间最初是根据其区间起始排序的。
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        length = len(intervals)
        if length < 1:
            return [newInterval]

        # 先把newInterval插入到intervals，使得intervals按照左区间是有序的。
        for i in range(length):
            if intervals[i].start >= newInterval.start:
                intervals.insert(i, newInterval)
                break
            if i == (length -1):
                intervals.append(newInterval)

        # 接下来跟56题一样，合并区间就行
        res = []
        curr = intervals[0]
        for i in range(length+1):
            # intervals[i].end >= curr.start 为什么错？
            if curr.end >= intervals[i].start:
                curr = Interval(curr.start, max(intervals[i].end, curr.end))
            else:
                res.append(curr)  
                curr = intervals[i]
        # 如果循环完成
        res.append(curr)
        return res
