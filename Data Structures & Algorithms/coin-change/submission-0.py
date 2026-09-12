class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        for i in range(0, len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)

        if dp[amount]==float('inf'):
            return -1

        return dp[amount]
        