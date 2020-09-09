class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    # in python next is a reversed word
    def reverse(self, head):
        if not head or not head.next:
            return head
        tempnode = ListNode(0)
        tempnode = self.reverse(head.next)  # 递归

        head.next.next = head
        head.next = None

        return tempnode

    # 迭代
    def reverse2(self, head):
        if not head or not head.next:
            return head
        # p q nextnode
        p = None
        q = head
        while q:
            nextnode = q.next
            q.next = p
            p = q
            q = nextnode
        return p







