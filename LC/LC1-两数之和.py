from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # {num : index}
        for i in range(len(nums)):
            if target - nums[i] not in hash_map:  # 对于nums[i]，若需找的另一数target - nums[i]暂不在字典中，nums[i]进字典
                hash_map[nums[i]] = i
            else:  # # 对于nums[i]，若需找的另一数target - nums[i]在字典中，返回索引
                return [i, hash_map[target - nums[i]]]



