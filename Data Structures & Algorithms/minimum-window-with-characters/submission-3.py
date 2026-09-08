class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {},{}
        #Crear mapa de counter de characters en t
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        res,resLen = [-1,-1], float("inf")
        need, have = len(countT), 0
        l = 0  

        for r in range(len(s)):
            #Agregar char actual a la ventana
            char = s[r]
            window[char] = window.get(char,0) + 1
            if char in countT and countT[char] == window[char]:
                have +=1
            #Mientras la ventana sea valida
            while have == need:
                #Calcular tamaño de la ventana
                windowSize = r-l + 1
                #Si la ventana es menor al mejor resultado, actualizar resultado
                if windowSize < resLen:
                    res = [l,r]
                    resLen = windowSize
                #remover leftmost char de la ventana
                leftMost = s[l]
                window[leftMost] -=1
                if leftMost in countT and window[leftMost]< countT[leftMost]:
                    have-=1
                l+=1
        l,r = res
        if resLen != float("inf"):
            return s[l:r+1]
        else: return ""
        