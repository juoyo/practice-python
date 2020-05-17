class Solution:
    def twoSum(self, nums, target):
        dict = {}  # 元素 ： 序号
        for i, num in enumerate(nums):
            another_num = target - num
            if another_num in dict:
                return [dict[another_num], i]
            dict[num] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))