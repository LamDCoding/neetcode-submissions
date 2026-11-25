class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 #creating a space for 26 entries for all the alphabets from a-z

            for c in s:
                count [ord(c) - ord("a")] +=1

            res[tuple(count)].append(s)

        return list(res.values())  #O(m #of solns/inputs *n #of length of words)  