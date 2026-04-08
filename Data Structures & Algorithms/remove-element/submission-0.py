class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #K will help us look for a number different than target, we start it at index 0
        k=0
        for num in nums:
        #Si el numero actual es diferente al valor
            if num != val:
            #Hacemos el cambio del index en el que vaya K con el numero actual
                nums[k] = num
            #Aumentamos el index de k
                k+=1
        return k
    
      


        