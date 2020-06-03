class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False
        return self.isPowerOfThree(n/3)

s = Solution()
print(s.isPowerOfThree(45))

print(10 / 3)
print(10 % 3)