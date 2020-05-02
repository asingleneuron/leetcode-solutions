# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    
    def linearSearch(self, n):
        """
            Doing a naive linear search starting from 1 to n. 
            Time comlexity : O(n)
        """
        for i in range(1, n+1):
            if isBadVersion(i):
                return i

    def binarySearchUtil(self, low, high):
        if low > high:
            return low
        else:
            mid = (low + high) // 2
            if isBadVersion(mid):
                return self.binarySearchUtil(low, mid - 1)
            else:
                return self.binarySearchUtil(mid + 1, high)

    def firstBadVersion_recursive(self, n):
        """
        :type n: int
        :rtype: int

        Approach:
            Doing binary search to find out the first bad version.
        
        Time complexity: O( log n)
        """
        return self.binarySearchUtil(1, n)

    def firstBadVersion_iterative(self, n):
        """
        :type n: int
        :rtype: int

        Approach:
           Doing binary search to find out the first bad version
        
        Time Complexity: O(log n)
        """
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            # print(low, high, mid)

            if isBadVersion(mid):
                high = mid - 1

            else:
                low = mid + 1

        return low

    def firstBadVersion(self, n):
        
#         return self.linearSearch(n)
#         return self.firstBadVersion_recursive(n)
        return self.firstBadVersion_iterative(n)




