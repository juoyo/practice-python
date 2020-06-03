from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ls = [0] * len((prices))
        for i in range(0, len(prices) - 1):  # 第i天买入
            ls[i] = max(prices[i + 1 : len(prices)]) - prices[i]  # 第i天买入的最大收益
        return max(ls)


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))