# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:

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
            I will use the binary search approach to find out the first bad version.
            n = 5
            1 2 3 4 5
            mid = n//2
            if mid==bad and mid-1 != bad , we found our first bad version
            if mid is bad then go to the first half
            else go to the second half
        """
        return self.binarySearchUtil(1, n)

    def firstBadVersion_iterative(self, n):
        """
        :type n: int
        :rtype: int

        Approach:
            I will use the binary search approach to find out the first bad version.
            n = 5
            1 2 3 4 5
            mid = n//2
            if mid==bad and mid-1 != bad , we found our first bad version
            if mid is bad then go to the first half
            else go to the second half

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
        return self.firstBadVersion_iterative(n)
        # return self.firstBadVersion_recursive(n)




