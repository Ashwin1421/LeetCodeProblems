class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)-1,-1,-1):
            result += s[i]
        
        return result