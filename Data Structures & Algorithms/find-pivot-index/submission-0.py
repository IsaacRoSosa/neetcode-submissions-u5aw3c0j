class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        #Switch array to prefix sum 
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        #Pass again array in search of pivot index 
        for i in range(len(nums)):
            left  = nums[i-1] if i > 0 else 0
            right = nums[-1] - nums[i] if i < len(nums) -1 else 0
            if left == right:
                return i
        return -1
