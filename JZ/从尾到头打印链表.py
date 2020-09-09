# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printListFromTailToHead(self, listNode):
    if not listNode:
        return []
    res = []
    while listNode:
        res.append(listNode.val)
        listNode = listNode.next
    return res

# 递归
result = []
def printListFromTailToHead2(self, listNode):
    if not listNode:
        return []
    if listNode:
        printListFromTailToHead2(listNode.next)
        result.append(listNode.val)  # 递归，开始元素在最后
    return result
