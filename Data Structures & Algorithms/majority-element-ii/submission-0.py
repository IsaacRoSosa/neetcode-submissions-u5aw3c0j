class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []

        counter = defaultdict(int)
        target = len(nums)/3
        for num in nums:
            counter[num] += 1
            if counter[num] > target and num not in ans:
                ans.append(num)       
        return ans
            

