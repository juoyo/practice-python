# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        cha = self.helper_height(root.left) - self.helper_height(root.right)
        return abs(cha) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper_height(self, root):  # 求以root为根节点的树高度
        if not root:
            return 0
        return 1 + max(self.helper_height(root.left), self.helper_height(root.right))




