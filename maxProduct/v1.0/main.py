class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (nums[len(nums) - 1] - 1) * (nums[len(nums) - 2] - 1)

#maxProdcuts on LC under Arrays
#Results
'''
Runtime: 40 ms, faster than 46.99% of Python online submissions for Maximum Product of Two Elements in an Array.
Memory Usage: 13.4 MB, less than 63.28% of Python online submissions for Maximum Product of Two Elements in an Array.
'''

'''
Comments
Could have definitely improved the runtime and memory usage. 
'''