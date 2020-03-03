class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            x = nums[i]
            digit = 1
            while x/10 > 0:
                digit += 1
                x = x/10
            if digit % 2 == 0:
                count += 1
        return count
              
