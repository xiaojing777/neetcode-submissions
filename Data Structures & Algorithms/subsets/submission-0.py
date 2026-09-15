class Solution:
    def backtracking(self, nums, path, result, start_index):
        result.append(path[:])

        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.backtracking(nums,path,result,i+1)
            path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backtracking(nums,path,result,0)
        return result
        