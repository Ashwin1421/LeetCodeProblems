class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits)-1,-1,-1):
        
            addOne = digits[i]+1
            carry = addOne//10
            digits[i] = addOne % 10
            if carry == 0:
                break
        
        if carry != 0:
            digits.append(digits[0])
            digits[0] = carry
        
        return digits
            