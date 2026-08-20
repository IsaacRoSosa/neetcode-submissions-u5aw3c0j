class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        #items() are returned based on the order of insertion
        i = 0
        
        for num, value in counter.items():
            if value >= 2:
                nums[i:i+2] = [num,num]
                i+=2
            else: 
                nums[i:i+value] = [num]
                i+=1
        return(i)

            
           