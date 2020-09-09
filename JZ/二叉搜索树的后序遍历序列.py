from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        self.helper(postorder)

    def helper(self, sequence):
        if len(sequence) <= 1:
            return True

        # 根据根节点，划分左右子树
        root = sequence[-1]
        for index in range(len(sequence)):
            if sequence[index] > root:
                break

        # 0到i-1为左子树，i到最后为右子树
        for j in range(index, len(sequence) - 1):
            if sequence[j] < root:
                return False

        # 递归左右子树是否为后序遍历序列
        return self.helper(sequence[:index]) and self.helper(sequence[index:-1])




