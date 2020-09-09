# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        if set(preorder) != set(inorder):
            return None
        root = TreeNode(preorder[0])
        pivot_index = inorder.index(preorder[0])  # inorder中，root以左为左子树，以右为右子树

        # 递归
        root.left = self.buildTree(preorder[1:pivot_index + 1], inorder[0:pivot_index])  # self.buildTree(左子树前序, 左子树中序)
        root.right = self.buildTree(preorder[pivot_index + 1:], inorder[pivot_index + 1:])

        return root









