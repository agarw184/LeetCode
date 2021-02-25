class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        boolarray = []
        if len(candies) > 100 or len(candies) < 2:
            return 
        elif extraCandies > 50 or extraCandies < 1:
            return 
        else:
            maxcandy = max(candies)
            for i in range(len(candies)):
                print(i)
                if candies[i] > 100 or candies[i] < 1:
                    return 
                else:
                    if (candies[i] + extraCandies) >= maxcandy:
                        boolarray.append(True)
                    else:
                        boolarray.append(False)
        return boolarray

#kidsWithCandies on LC under Arrays
#Results
'''
Runtime: 28 ms, faster than 49.22% of Python online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 13.4 MB, less than 43.36% of Python online submissions for Kids With the Greatest Number of Candies.
'''

'''
Comments
Could have definitely improved the runtime and memory usage. 
'''