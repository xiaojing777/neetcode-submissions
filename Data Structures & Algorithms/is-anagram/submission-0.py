class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table = [0]*26
        for char in s:
            hash_table[ord(char)-ord('a')] += 1

        for char in t:
            hash_table[ord(char)-ord('a')] -= 1
        
        for num in hash_table:
            if num!=0:
                return False
        
        return True
        