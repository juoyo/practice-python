class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        head = ListNode(-1)
        head.next = pHead

        pre = head
        p = head.next

        while p and p.next:
            if p.val == p.next.val:
                while p.next and p.val == p.next.val:
                    p.next = p.next.next
                pre.next = p.next
                p = p.next
            else:
                pre = pre.next
                p = p.next

        return head.next







