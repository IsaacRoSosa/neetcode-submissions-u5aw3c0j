class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxCount = 0

        for num in nums:
            if num:
                count +=1
            else:
                count = 0

            if count >= maxCount:
                maxCount = count


        return maxCount
        