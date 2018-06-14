class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr = ""
        for char in s:
            if char.isalnum():
                newstr += char.lower()

        isPalindrome = lambda x: x == x[::-1]
        
        return isPalindrome(newstr)