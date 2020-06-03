class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 循环迭代
        if n < 1:
            return False
        while n % 3 == 0:
            n = n / 3
        return n == 1

s = Solution()
print(s.isPowerOfThree(45))
