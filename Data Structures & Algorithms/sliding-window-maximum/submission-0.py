import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        result = []

        for i,num in enumerate(nums):
            while q and num>nums[q[-1]]:
                q.pop()
            
            q.append(i)

            if i-q[0]>=k:
                q.popleft()
            
            if i>=k-1:
                result.append(nums[q[0]])
        
        return result


            
        