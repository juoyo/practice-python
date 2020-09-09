class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k < 1:
            return None

        p = head
        q = head

        for i in range(k - 1):  # 0,k-2
            if not q.next:
                return
            q = q.next

        while q.next:
            p = p.next
            q = q.next

        return p




