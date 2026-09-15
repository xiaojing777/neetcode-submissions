import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pri_q = nums
        heapq.heapify(pri_q)
        while len(pri_q)>k:
            heapq.heappop(pri_q)
        
        return pri_q[0]
        