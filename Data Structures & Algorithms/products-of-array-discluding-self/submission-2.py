class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroCount = 0
        for num in nums: 
            if num: 
                total = total * num
            else:
                zeroCount += 1

        ans = [0] * len(nums)
        if zeroCount > 1:
            return ans
        
        for i,num in enumerate(nums):
            if zeroCount:
                if num:
                    ans[i] = 0
                else:
                    ans[i] = total
            else:
                ans[i] = total//num
        return ans