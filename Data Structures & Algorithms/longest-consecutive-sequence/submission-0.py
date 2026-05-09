class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        digits = set(nums)
        ans = 0
        for num in nums:
            #Empieza la secuencia 
            if num-1 not in digits: 
                count = 0
                while num in digits:
                    num += 1
                    count += 1
                ans = max(ans, count)
            else:
                continue
        return ans

