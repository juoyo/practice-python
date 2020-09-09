# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root:
            self.DFS([], root, sum)
        return self.res

    # DFS递归写法
    def DFS(self, trace, node, num):
        if node.val == num and not node.left and not node.right:
            trace.append(node.val)
            self.res.append(trace)

        if node.left:
            self.DFS(trace + [node.val], node.left, num - node.val)

        if node.right:
            self.DFS(trace + [node.val], node.right, num - node.val)








