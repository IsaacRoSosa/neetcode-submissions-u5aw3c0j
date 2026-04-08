class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = defaultdict(int)
        w2 = defaultdict(int)

        for char in s:
            w1[char] += 1
        for char in t:
            w2[char] += 1
        
        return w1 == w2