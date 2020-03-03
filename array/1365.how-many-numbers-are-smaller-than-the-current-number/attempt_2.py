class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        m = []
        sorted_nums = sorted(nums)
        for i in range(n):
            a = bisect.bisect_left(sorted_nums, nums[i])
            m.append(a)
        return m
