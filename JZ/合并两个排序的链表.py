# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        # 递归
        mergeHead = None
        if l1.val < l2.val:
            mergeHead = l1
            mergeHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            mergeHead = l2
            mergeHead.next = self.mergeTwoLists(l1, l2.next)

        return mergeHead

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 迭代
        mergeHead = ListNode(0)
        dum = mergeHead  # 记录新链表首节点
        while l1 and l2:
            if l1.val < l2.val:
                mergeHead.next = l1
                l1 = l1.next
                # mergeHead = mergeHead.next
            else:
                mergeHead.next = l2
                l2 = l2.next
                # mergeHead = mergeHead.next
            mergeHead = mergeHead.next  # 处理新链表下个节点
        if not l1:
            mergeHead.next = l2
        if not l2:
            mergeHead.next = l1

        return dum















