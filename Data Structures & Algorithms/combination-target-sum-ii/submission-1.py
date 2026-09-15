class Solution:
    def backtracking(self, candidates, target, path, result, start_index):
        if sum(path)==target:
            result.append(path[:])
            return
        if sum(path)>target:
            return
        for i in range(start_index, len(candidates)):
            if i>start_index and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            self.backtracking(candidates,target,path,result,i+1)
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        used = set()
        self.backtracking(candidates, target, path, result, 0)
        return result
        