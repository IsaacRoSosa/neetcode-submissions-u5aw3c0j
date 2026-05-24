class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        i = 0
        while counter[0] > 0:
            nums[i] = 0
            i+=1
            counter[0]-=1
        #Convert 1
        while counter[1] > 0:
            nums[i] = 1
            i+=1
            counter[1]-=1
        #Convert 2
        while counter[2] > 0:
            nums[i] = 2
            i+=1
            counter[2]-=1

