class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for i in nums:
            if seen.get(i) is None:
                seen[i] = 1
            else:
                seen[i] += 1

        for i in nums:
            if seen[i] == 1:
                return i
