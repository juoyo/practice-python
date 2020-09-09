# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check_symmetric(root.left, root.right)

    def check_symmetric(self, L, R):  # 可以判断L、R是否相等
        # 递归出口
        if not L and not R:
            return True
        elif not L or not R:
            return False

        if L.val != R.val:
            return False
        else:
            # 根节点相等，递归判断左右子树
            return self.check_symmetric(L.left, R.right) and self.check_symmetric(L.right, R.left)









