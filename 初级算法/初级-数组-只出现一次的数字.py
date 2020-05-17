class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] = nums[0] ^ nums[i]
        return nums[0]





s = Solution()
print(s.singleNumber([2, 2, 1, 3, 1, 5, 5]))


print(2 and 2)