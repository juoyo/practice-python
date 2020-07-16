'''
主要思路：
入队时
1.直接push到inStack中
出队时
1.如果outStack为空，先把inStack所有元素逐一弹出，push到outStack，最后弹出outStack的栈顶元素
2.如果outStack不为空，直接弹出outStack的栈顶元素
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        # if not self.stack2:
        #     while self.stack1:
        #         self.stack2.append(self.stack1.pop())
        # return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        # if not self.stack2:
        #     while self.stack1:
        #         self.stack2.append(self.stack1.pop())
        # return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # if self.stack1 == [] and self.stack2 == []:
        #     return True
        # else:
        #     return False
        return not self.stack1 and not self.stack2



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()