class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        numCount = Counter(nums)
        ans = []

        for num,count in numCount.items():
            if count > len(nums)/3:
                ans.append(num)
        return ans