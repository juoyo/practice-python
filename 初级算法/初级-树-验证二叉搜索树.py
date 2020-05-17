# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, node, lower=float('-inf'), upper=float('inf')):
        if node is None:
            return True
        if node.val <= lower or node.val >= upper:
            return False

        if self.helper(node.left, lower, node.val) == False:
            return False
        if self.helper(node.right, node.val, upper) == False:
            return False

        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))


root = TreeNode(2)
l = TreeNode(1)
r = TreeNode(3)
root.left = l
root.right = r

s = Solution()
print(s.isValidBST(root))

