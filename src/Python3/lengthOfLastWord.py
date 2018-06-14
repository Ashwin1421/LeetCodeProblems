class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) >= 1 and not s.isspace():
            return len(s.split()[-1])
        else:
            return 0