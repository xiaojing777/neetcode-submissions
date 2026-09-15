import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {}
        for num in nums:
            freq_dic[num] = freq_dic.get(num, 0)+1
        
        pri_q = []
        for num,freq in freq_dic.items():
            heapq.heappush(pri_q, (freq, num))
        
        while len(pri_q)>k:
            heapq.heappop(pri_q)
        
        result = []
        for freq,num in pri_q:
            result.append(num)
        
        return result

        