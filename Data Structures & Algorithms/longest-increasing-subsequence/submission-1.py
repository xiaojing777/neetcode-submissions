class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        result = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i]>result:
                        result = dp[i]
        return result