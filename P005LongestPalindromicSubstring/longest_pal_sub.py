# 最长回文子串
# 枚举每一个字符是回文字符串中心，然后分两种情况：
# 如果回文字符串是长度是奇数，
# 如果回文字符串是长度是偶数，

class Solution:
    # 中心枚举
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
            
        max_length = 0
        palindrome = ''
        for i in range(len(s)):
            # 如果是奇数回文串
            x = 1
            while (i-x) >= 0 and (i+x) < len(s):
                if s[i-x] == s[i+x]:
                    x += 1
                else:
                    break
            x -= 1
            if (2*x + 1) > max_length:
                max_length = 2*x + 1
                palindrome = s[i-x: i+x+1]
            
            # 如果是偶数回文串
            x = 0
            while (i-x)>=0 and (i+x+1) <len(s):
                if s[i-x] == s[i+x+1]:
                    x += 1
                else:
                    break
            x -= 1
            if 2*x + 2 > max_length:
                max_length = 2*x +2
                palindrome = s[i-x: i+x+2]
        # 如果遍历完都还是空，说明单个字符就是最大回文串了   
        if palindrome == '':
            return s[0]
        return palindrome

string1 = "babad"
string2 = "cbbd"

for st in ["babad", "cbbd"]:
    obj = Solution().longestPalindrome(st)
    print(obj)
