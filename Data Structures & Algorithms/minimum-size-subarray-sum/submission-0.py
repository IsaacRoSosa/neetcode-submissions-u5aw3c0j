class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0 
        n = len(nums)
        length = n + 1

        for R in range(n):
            total += nums[R]
            while total >= target:
                length = min(R-L + 1,length)
                total -= nums[L]
                L += 1
        return 0 if length == n + 1 else length