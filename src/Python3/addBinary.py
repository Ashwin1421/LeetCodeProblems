class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxlen = max(len(a), len(b))
        a = a.zfill(maxlen)
        b = b.zfill(maxlen)
        result = ""
        carry = 0
        for i in range(maxlen-1,-1,-1):
            res = carry
            res += 1 if a[i] == "1" else 0
            res += 1 if b[i] == "1" else 0
            result = ("1" if res % 2 == 1 else "0") + result
            carry = 0 if res < 2 else 1

        if carry != 0:
            result = "1" + result

        return result.zfill(maxlen)