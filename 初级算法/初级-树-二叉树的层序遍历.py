# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        ls = []
        ls.append(root)

        while ls:
            Temp = []
            tempres = []
            while ls:
                t = ls.pop(0)
                Temp.append(t)
                tempres.append(t.val)
            if tempres:
                res.append(tempres)
            while Temp:
                temp = Temp.pop(0)
                if temp.left:
                    ls.append(temp.left)
                if temp.right:
                    ls.append(temp.right)
        return res

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5

s = Solution()
print(s.levelOrder(node1))






