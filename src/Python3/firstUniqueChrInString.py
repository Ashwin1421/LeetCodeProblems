class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {}
        for c in s:
            if c not in charMap:
                charMap[c] = 1
            else:
                charMap[c] += 1
        
        for c in s:
            if charMap[c] == 1:
                #print(k)
                return s.index(c)
        
        return -1