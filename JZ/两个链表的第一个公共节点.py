# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 每个链表走完自己的路后，从头开始走对方的路，当二者相遇（相等）时，要不然就是相交了，要不然就是同时到了另一个尽头（None）了：因为彼此走的路都是相同长度。
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa = headA
        pb = headB

        while pa != pb:  # 若无交点，最后pa = pb = none
            if pa:
                pa = pa.next
            else:
                pa = pb

            if pb:
                pb = pb.next
            else:
                pb = pa
            # pa = (pa.next if pa else pb)
            # pb = (pb.next if pb else pa)

        return pa  # pa、pb相交




