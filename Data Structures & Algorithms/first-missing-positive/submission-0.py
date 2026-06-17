class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        seenNums = set(nums)
        ans = 1

        while ans in seenNums:
            ans+=1

        return(ans)
        
        