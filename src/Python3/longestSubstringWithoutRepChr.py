class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        match, res = -1, 0
        charMap = {}
        for i in range(len(s)):
            if s[i] in charMap and match < charMap[s[i]]:
                match = charMap[s[i]]
            res = max(res, i-match)
            charMap[s[i]] = i
        
        print(res)
        return res