class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        m = []
        i = 0
        while i < n:
            f = nums[i]
            v = nums[i+1]
            m += [v] * f
            i += 2
        return m
