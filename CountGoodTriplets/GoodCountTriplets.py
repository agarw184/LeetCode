#LC problem = 1534

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        if len(arr) == 0:
            return 0
        else:
            count = 0
            for i in range(len(arr)):
                j = i + 1
                while j < len(arr):
                    k = j + 1
                    while k < len(arr):
                        if ((abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (
                                abs(arr[i] - arr[k]) <= c)):
                            count = count + 1
                        k = k + 1
                    j = j + 1
            return count

#Results
"""
Runtime: 560 ms, faster than 54.46% of Python online submissions for Count Good Triplets.
Memory Usage: 13.4 MB, less than 64.45% of Python online submissions for Count Good Triplets.
"""
