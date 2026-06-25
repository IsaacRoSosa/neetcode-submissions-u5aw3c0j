class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r-l) //2)
            #Si es mayor
            if nums[m] > target:
                r = m-1
            #Si el numero es menor
            elif nums[m] < target:
                l = m+1
            else:
                return m

        return -1
        