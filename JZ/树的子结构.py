# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 若树 BB 是树 AA 的子结构，则必满足以下三种情况之一，因此用或 || 连接；
# 以 节点 AA 为根节点的子树 包含树 BB ，对应 helper(A, B)；
# 树 BB 是 树 AA 左子树 的子结构，对应 isSubStructure(A.left, B)；
# 树 BB 是 树 AA 右子树 的子结构，对应 isSubStructure(A.right, B)；


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:  # 判断B是否是A的子结构
        '''
        :param A:
        :param B:
        :return:
        '''
        if not A or not B:
            return False

        # flag = False
        # if A.val == B.val:
        #     flag = self.helper(A, B)
        # if not flag:
        #     flag = self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        # return flag
        return self.helper(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def helper(self, P, Q):  # 判断Q是否是以（P的根节点）为根节点的子树
        if not Q:
            return True
        elif not P:
            return False
        elif P.val != Q.val:
            return False
        else:  # P.val == Q.val，判断左右子树是否相等
            return self.helper(P.left, Q.left) and self.helper(P.right, Q.right)








