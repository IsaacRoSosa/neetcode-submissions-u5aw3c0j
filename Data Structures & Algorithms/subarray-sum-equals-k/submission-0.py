class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSum = {0:1} #PrefixSum, Counter
        curSum = 0
        ans = 0
        for num in nums:
            curSum += num
            dif =curSum - k
            ans += prefSum.get(dif,0)
            prefSum[curSum] = 1 + prefSum.get(curSum,0)
        return ans 