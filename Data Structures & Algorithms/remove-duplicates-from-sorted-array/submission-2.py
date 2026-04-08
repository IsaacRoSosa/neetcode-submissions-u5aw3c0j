class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        #Mientras recorremos el arreglo
        while r < n:
            #realizamos el cambio
            nums[l] = nums[r]
            #Buscamos el proximo numero unico
            while r < n and nums[l] == nums[r]:
                r += 1
            l += 1
        return l 