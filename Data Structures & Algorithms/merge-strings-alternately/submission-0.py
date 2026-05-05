class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans = []
        index = 0
        while index < min(len(word2),len(word1)):
            ans.append(word1[index])
            ans.append(word2[index])
            index += 1
        
        #Despues del while, agregamos lo que quede 
        ans.append(word1[index:])
        ans.append(word2[index:])




        return "".join(ans)