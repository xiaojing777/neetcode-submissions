dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

class Solution:
    def backtracking(self, digits, path, result, index):
        if index==len(digits):
            result.append(path[:])
            return
        cur_digit = digits[index]
        for i in range(len(dic[cur_digit])):
            path = path+dic[cur_digit][i]
            self.backtracking(digits, path, result, index+1)
            path = path[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        path = ""
        result = []
        self.backtracking(digits,path,result,0)
        return result
        