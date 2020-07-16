from heapq import *
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(self.nums)  # 所有元素建立小顶堆
        while len(self.nums) > self.k:  # 缩减小顶堆大小到k
            heappop(self.nums)  # 去掉小顶堆堆顶元素，出栈

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
            heapify(self.nums)
        else:
            top = self.nums[0]  # 取小顶堆堆顶元素
            if top < val:  # 若堆顶元素小于新加元素，新加元素替换堆顶元素，重新形成小顶堆
                heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)