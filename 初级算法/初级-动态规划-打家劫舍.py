class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n_len = len(nums)
        if n_len == 1:
            return nums[0]
        if n_len == 2:
            return max(nums[0], nums[1])

        # 状态定义
        dp = [0] * n_len

        # 初始状态
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # 状态转移方程
        for i in range(2, n_len):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n_len - 1]

