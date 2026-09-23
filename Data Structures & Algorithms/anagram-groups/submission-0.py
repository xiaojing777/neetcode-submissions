class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        result = []

        for str in strs:
            hash_table = [0]*26
            for char in str:
                hash_table[ord(char)-ord('a')] += 1
            key = tuple(hash_table)
            if key not in dic:
                dic[key] = [str]
            else:
                dic[key].append(str)
        
        for str_list in dic.values():
            result.append(str_list)
        
        return result
            
        