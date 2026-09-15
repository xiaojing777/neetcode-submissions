class Solution:
    def backtracking(self, nums, path, result, used):
        if len(path)==len(nums):
            result.append(path[:])
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            path.append(nums[i])
            used.add(nums[i])
            self.backtracking(nums,path, result, used)
            path.pop()
            used.remove(nums[i])

    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = set()
        self.backtracking(nums, path, result, used)
        return result

        