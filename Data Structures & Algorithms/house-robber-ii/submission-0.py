class Solution:
    def robline(self, nums, start, end):
        if end==start:
            return nums[start]
        dp = [0]*(end-start+1)
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start+1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[start+i])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res1 = self.robline(nums, 0, len(nums)-2)
        res2 = self.robline(nums, 1, len(nums)-1)
        return max(res1, res2)
        