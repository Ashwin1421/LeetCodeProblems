class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 != 0:
            return nums[(len(nums)-1)//2]/1.0
        else:
            a = nums[(len(nums)-1)//2]
            b = nums[((len(nums)-1)//2)+1]
            return (a+b)/2