class Solution:
    def climbStairs(self, n: int) -> int:
        # 状态定义
        dp = [0] * (n + 1)  # 0~n-1表示1~n阶台阶的走法

        # 初始状态
        dp[0] = 1
        dp[1] = 2

        if n <= 2:
            return dp[n - 1]

        # DP状态推导
        for i in range(2, n):  # [2, n-1]
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


s = Solution()
print(s.climbStairs(4))