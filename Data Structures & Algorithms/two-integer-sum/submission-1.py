class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        missing = {}
        for index,num in enumerate(nums):
            dif = target - num
            if num in missing:
                print("found")
                return[missing[num],index]
            else:
                missing[dif] = index 
        print(missing)



        