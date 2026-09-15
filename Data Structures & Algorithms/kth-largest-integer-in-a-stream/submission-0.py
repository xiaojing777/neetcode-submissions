import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pri_queue = nums
        heapq.heapify(self.pri_queue)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.pri_queue, val)
        while len(self.pri_queue)>self.k:
            heapq.heappop(self.pri_queue)
        return self.pri_queue[0]

        
