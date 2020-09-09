from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []  # 记录已访问路径

        self.backtrack(nums, track)

        return self.res

    def backtrack(self, nums, track):
        # 结束条件
        if len(track) == len(nums):
            self.res.append(track[:])
            return

        for i in range(0, len(nums)):
            if nums[i] in track:  # 已访问节点略过
                continue

            # 访问路径加入节点，做出选择
            track.append(nums[i])

            # 进入下一层决策树
            self.backtrack(nums, track)

            # 访问路径回退，取消选择，恢复状态
            track.pop()

s = Solution()
print(s.permute([1, 2, 3]))
