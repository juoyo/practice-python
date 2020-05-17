class Solution:
    def containsDuplicate(self, nums):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return False
        return True

s = Solution()
print(s.containsDuplicate([3,1]))
print(len([]))