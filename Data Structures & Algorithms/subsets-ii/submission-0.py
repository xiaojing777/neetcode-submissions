class Solution:
    def backtracking(self, nums, path, result, start_index):
        result.append(path[:])
        for i in range(start_index, len(nums)):
            if i>start_index and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums,path,result,i+1)
            path.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        result = []
        self.backtracking(nums, path, result, 0)
        return result

        