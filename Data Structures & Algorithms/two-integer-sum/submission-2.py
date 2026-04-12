class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for index, number in enumerate(nums):
            complement = target-number
            if complement in pairs:           
                return [pairs[complement],index]
            else:
                pairs[number] = index 

        
            