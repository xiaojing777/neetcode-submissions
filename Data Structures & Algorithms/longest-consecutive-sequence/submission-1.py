class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        nums_set = set(nums)
        result = 1

        for num in nums_set:
            if num-1 not in nums_set:
                length = 1
                while num+1 in nums_set:
                    num+=1
                    length += 1
                result = max(result, length)
        
        return result
        