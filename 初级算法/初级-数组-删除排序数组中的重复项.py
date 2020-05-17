class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # i记录最后一个不同数的下标
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # 遍历直到找到一个和当前最后不同数不一样的新数，新数作为当前最后的不同数的下标
                i = i + 1
                nums[i] = nums[j]
        return i + 1

s = Solution()
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))





