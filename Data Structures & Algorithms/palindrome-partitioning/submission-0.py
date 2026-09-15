class Solution:
    def isPalindrome(self, s, start, end):
        if end<=start or not s:
            return True
        l = start
        r = end
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        
        return True

    def backtracking(self, s, path, result, start_index):
        if start_index == len(s):
            result.append(path[:])
            return

        for i in range(start_index, len(s)):
            if self.isPalindrome(s, start_index, i):
                path.append(s[start_index:i+1])
                self.backtracking(s, path, result, i+1)
                path.pop()

    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        self.backtracking(s, path, result, 0)
        return result
        