class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        #Creamos buckets del 0 al tamaño del array
        freq = [[] for i in range(len(nums)+ 1)]
        
        for n in nums:
            #get(key, val) Val es para regresar un valor en caso de que no exista
            counter[n] = 1 + counter.get(n, 0)
        #Armamos el freq counter 
        for num, con in counter.items():
            freq[con].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

       




        
        