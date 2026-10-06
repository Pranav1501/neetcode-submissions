class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            dic[char] =  dic.get(char,0) + 1
        for char in t:
            dic[char] =  dic.get(char,0) - 1
            
        return all(v == 0 for v in dic.values())



