class Solution:
    def backtracking(self, nums, target, path, result, start_index):
        if sum(path)==target:
            result.append(path[:])
            return
        if sum(path)>target:
            return

        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, target, path, result, i)
            path.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        self.backtracking(nums, target, path, result, 0)
        return result
        