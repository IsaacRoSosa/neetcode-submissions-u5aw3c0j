# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mSort(arr, s, m, e):
            #Build left and right side
            L = arr[s: m+1]
            R = arr[m+1: e+1]
            #Pointers
            i = j = 0
            k = s
            #Mientras haya elementos en ambos arrays ir sorteando
            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    arr[k] = L[i]
                    i +=1
                else:
                    arr[k] = R[j]
                    j +=1
                k+=1
            #Cuando solo queden elementos de un array
            while i < len(L):
                arr[k] = L[i]
                i+=1
                k+=1
            while k < len(R):
                arr[k] = R[j]
                j+=1
                k+=1

        
        def mergeSor(arr, s, e):
            #base case 
            if e - s + 1 <= 1:
                return arr
            #middle Index 
            m = (s + e) //2
            #Left Side
            mergeSor(arr, s, m)
            #Right Side
            mergeSor(arr, m+1 , e)
            #sort
            mSort(arr, s, m, e)

            return arr

        return mergeSor(pairs, 0, len(pairs))

         

