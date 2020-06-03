class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        count = 0
        for i in bin(res):
            if i == '1':
                count = count + 1
        return count




s = Solution()
print(s.hammingDistance(93, 73))
