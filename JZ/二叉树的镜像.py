# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root.left or not root.right:
            return root

        # 交换左右子树
        temp = root.left
        root.left = root.right
        root.right = temp

        # 递归左右子树，交换左右子树内部的左右子树
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        return root

    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        leftRoot = self.mirrorTree(root.right)
        rightRight = self.mirrorTree(root.left)

        root.left = leftRoot
        root.right = rightRight

        return root


