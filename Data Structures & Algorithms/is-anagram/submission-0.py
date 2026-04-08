class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))

        if (len(s) != len(t)):
            return False

        for i in range(len(sortedS)):
            if (sortedS[i] != sortedT[i]):
                return False
        return True
        
