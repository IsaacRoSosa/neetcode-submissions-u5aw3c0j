class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
          
        #guardamos los numeros a utlizar del array nums1
        L = nums1[0:m]
        #Pointers
        i = j = k = 0
        #Mientras haya elementos en ambos arrays ir comparando y sorteando 
        while i < m and j < n:
            if L[i] <= nums2[j]:
                nums1[k] = L[i]
                i +=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1

        while i < m:
            nums1[k] = L[i]
            i +=1
            k+=1

        while j < n:
            nums1[k] = nums2[j]
            j+= 1
            k+=1
        
