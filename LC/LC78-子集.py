from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        last_num = nums.pop(-1)
        res = self.subsets(nums)
        for i in range(len(res)):
            temp = res[i][:]  # 切片不改变原有res[i]
            temp.append(last_num)
            res.append(temp)
        return res
s = Solution()
print(s.subsets([1, 2]))


