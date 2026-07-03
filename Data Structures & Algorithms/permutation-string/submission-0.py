class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        n = len(s1)
        i=0
        while (i + n-1) < len(s2):
            
            if counter1 == Counter(s2[i:i+n]):
                return True

            i+=1
        return False
        