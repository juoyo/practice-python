from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if index2 < 0 or (index1 >= 0 and index2 >= 0 and nums1[index1] > nums2[index2]):
                nums1[i] = nums1[index1]
                index1 = index1 - 1
            elif index1 < 0 or (index1 >= 0 and index2 >= 0 and nums1[index1] <= nums2[index2]):
                nums1[i] = nums2[index2]
                index2 = index2 - 1

        return nums1

s = Solution()
print(s.merge([2, 0], 1, [1], 1))





