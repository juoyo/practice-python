# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 判断两棵树是否对称
    def helper(self, t1, t2):
        # 如果两棵树均为空，返回True
        if t1 is None and t2 is None:
            return True
        # 如果两棵树中有一棵为空，返回False
        if t1 is None or t2 is None:
            return False
        # 如果两棵树均不空，但值不想等，返回False
        if t1.val != t2.val:
            return False

        if self.helper(t1.left, t2.right) and self.helper(t1.right, t2.left):
            return True
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helper(root.left, root.right)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node1.left = node2
node1.right = node3
s = Solution()
print(s.isSymmetric(node1))



