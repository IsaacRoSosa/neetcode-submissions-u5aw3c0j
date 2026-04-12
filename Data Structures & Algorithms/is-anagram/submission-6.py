class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        for char in s:
            counter1[char] +=1
        
        for char in t:
            counter2[char] +=1

        return counter1 == counter2

            