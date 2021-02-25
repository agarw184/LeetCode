class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        else:
            i = 0
            k = len(nums)
            arraysum = 0
            while (i < len(nums)):
                arraysum = arraysum + nums[i]
                nums[i] = arraysum
                i = i + 1
            return nums

#Running sum problem on LC under Arrays
#Results
'''
Runtime: 28 ms, faster than 57.41% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 13.5 MB, less than 68.95% of Python online submissions for Running Sum of 1d Array.
'''