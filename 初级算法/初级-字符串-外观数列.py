class Solution:
    def countAndSay(self, n: int) -> str:
        dp = [ '0' ] * (n + 1)
        dp[1] = '1'
        dp[2] = '11'
        dp[3] = '21'
        for i in range(2, n + 1):
            for j in range(len(dp[i - 1])):
                pass



