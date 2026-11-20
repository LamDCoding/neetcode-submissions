class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash = {}

        for char in s:
            hash[char] = hash.get(char, 0) + 1
        
        for char in t:
            hash[char] = hash.get(char, 0) - 1
            if hash[char] < 0:
                return False
        
        return True