class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        print(nums[0 : k])
        nums[0 : k].reverse()

        nums[k : -1].reverse()
        print(nums)


s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))


