class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)/2
        m = []
        for i in range(n):
            f = nums[2*i]
            v = nums[2*i+1]
            for j in range(f):
                m.append(v)
        return m
