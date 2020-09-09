
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        self.pre_node = Node(-1)
        self.head = Node(-1)

        self.midorder(root)

        # 中序遍历完成，首尾节点相连
        self.head.left = self.pre_node
        self.pre_node.right = self.head
        return self.head

    def midorder(self, cur_root): # 中序遍历
        if not cur_root:
            return

        self.midorder(cur_root.left)  # 递归左子树

        if self.pre_node:
            self.pre_node.right = cur_root
            cur_root.left = self.pre_node
        else:  # 记录头节点
            self.head = cur_root
        self.pre_node = cur_root

        self.midorder(cur_root.right)  # 递归右子树








