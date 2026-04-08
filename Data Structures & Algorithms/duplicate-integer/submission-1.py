class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #ordenamos el arreglo en orden ascendente
        nums.sort()
        #recorremos todo el arreglo
        for i in range(len(nums)):
            #Si no estamos en el ultimo elemento
            if i < len(nums) - 1:
                if nums[i+1] == nums[i]:
                    #si es igual regresamos falso
                    return True
        return False
            
    

         