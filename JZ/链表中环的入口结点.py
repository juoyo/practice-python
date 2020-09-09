# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return pHead

        head = ListNode(0)
        head.next = pHead

        fast = head
        slow = head

        # 循环
        while True:
            if fast and fast.next:
                fast = fast.next.next  # 快指针一次2步
                slow = slow.next  # 慢指针一次1步
            else:
                return None

            if fast == slow:  # 快慢指针相遇时，len(快) = 2 * len(慢)
                fast = head  # 快指针再从头走
                break

        while fast != slow:  # fast、slow相遇在环的入口
            fast = fast.next
            slow = slow.next

        return fast





















