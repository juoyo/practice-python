# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def helper(self, nums, left, right):
        if left > right:
            return None
        # always choose left middle node as a root
        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid - 1)
        root.right = self.helper(nums, mid + 1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
        return self.helper(nums, 0, len(nums) - 1)
