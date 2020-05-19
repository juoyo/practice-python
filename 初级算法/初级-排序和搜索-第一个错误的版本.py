# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n

        while i < j:
            mid = i + (j - i) // 2
            if isBadVersion(mid):
                j = mid
            else:
                i = mid + 1
        return i



