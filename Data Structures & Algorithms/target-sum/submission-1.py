class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums)+target)%2==1:
            return 0
        real_target = (sum(nums)+target)//2
        if real_target<0:
            return 0

        dp = [0]*(real_target+1)
        dp[0] = 1
        
        for i in range(len(nums)):
            for j in range(real_target, nums[i]-1, -1):
                dp[j] = dp[j]+dp[j-nums[i]]
        
        return dp[real_target]

        