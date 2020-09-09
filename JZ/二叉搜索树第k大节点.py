class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root or not k:
            return None
        self.res = []
        self.midorder(root)
        if len(self.res) < k:
            return None
        return self.res[len(self.res) - k]

    # 中序遍历
    def midorder(self, root):
        if not root:
            return

        self.midorder(root.left)

        self.res.append(root.val)

        self.midorder(root.right)









