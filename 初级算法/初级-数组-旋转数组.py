class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            temp = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = temp
        return nums

s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))
