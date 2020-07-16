class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(0, len(self.queue1) - 1):  # queue1除队尾元素外，进入queue2，queue1队尾元素变队头
            self.queue2.append(self.queue1.pop(0))
        if not self.queue1:
            for j in range(0, len(self.queue2)):  # queue2所有元素入queue1
                self.queue1.append(self.queue2.pop(0))
            for i in range(0, len(self.queue1) - 1):  # queue1除队尾元素外，进入queue2，queue1队尾元素变队头
                self.queue2.append(self.queue1.pop(0))
        return self.queue1.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        for i in range(0, len(self.queue1) - 1):  # queue1除队尾元素外，进入queue2，queue1队尾元素变队头
            self.queue2.append(self.queue1.pop(0))
        if not self.queue1:
            for j in range(0, len(self.queue2)):  # queue2所有元素入queue1
                self.queue1.append(self.queue2.pop(0))
            for i in range(0, len(self.queue1) - 1):  # queue1除队尾元素外，进入queue2，queue1队尾元素变队头
                self.queue2.append(self.queue1.pop(0))
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue1 == [] and self.queue2 == []

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.empty())
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()