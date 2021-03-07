
#LC problem - 1486

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = list()
        for i in range(n):
            nums.append(start + 2*i)
            
        temp = 0
        for i in nums:
            temp ^= i
        return temp

#Reuslts 
# Runtime: 16 ms, faster than 76.78% of Python online submissions for XOR Operation in an Array.
# Memory Usage: 13.5 MB, less than 45.70% of Python online submissions for XOR Operation in an Array.