"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?

这道题说有个数据流每次提供一个数字，然后让我们组成一系列分离的区间，这道题跟之前那道Insert Interval很像，思路也很像，每进来一个新的数字val，我们都生成一个新的区间[val, val]，然后将其插入到当前的区间里，
注意分情况讨论，无重叠，相邻，和有重叠分开讨论处理，
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """ 
        self.intervals = []

    def addNum(self, val: int):
        res = []
        curr = Interval(val,val)
        pos = 0
        for i in self.intervals:
            # +1 是为了避免 判断完全隔开
            if curr.end+1 < i.start:
                res.append(i)
            elif i.end+1 < curr.start:
                res.append(i)
                pos += 1
            else:
                curr.start = min(i.start, curr.start)
                curr.end = max(i.end, curr.end)
        res.insert(pos, curr)
        self.intervals = res

    def getIntervals(self):
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()