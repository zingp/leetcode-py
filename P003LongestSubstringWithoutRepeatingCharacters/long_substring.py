# 最长无重复子串
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
HashMap + 滑动窗口
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLen = 0    # start 是左指针，max_len 是最长长度
        useDic = {}
        for i, v in enumerate(s):
            # 如果v在dic中，说明遇到了重复的字符串，需要移动左指针
            if v in useDic and start <= useDic[v]:
                start = useDic[v] + 1
            # 当前长度是右指针-左指针+1，与历史最长相比取大者
            maxLen = max(maxLen, i - start + 1)
            useDic[v] = i
        return maxLen

    def lengthOfLongestSubstring2(self, s):
        useDic = {}
        res = i = j = 0
        for m in s:
            if m in useDic:
                i = i if i>useDic[m] else useDic[m]
            res= res if res>=(j-i+1) else (j-i+1)
            useDic[m] = j + 1
            j += 1
        return res
                
s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))


