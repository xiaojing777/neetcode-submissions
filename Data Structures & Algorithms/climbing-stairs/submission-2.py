class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n

        dp = [0]*2
        dp[0] = 1
        dp[1] = 2
        for i in range(3, n+1):
            tmp = dp[0]
            dp[0] = dp[1]
            dp[1] = tmp+dp[0]
        return dp[1]
        # dp = [0]*(n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-2]+dp[i-1]

        # return dp[n]
        