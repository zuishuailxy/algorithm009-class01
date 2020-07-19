class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = collections.Counter(s)
        for idx, val in enumerate(s):
            if hashmap[val] == 1:
                return idx
        
        return -1 