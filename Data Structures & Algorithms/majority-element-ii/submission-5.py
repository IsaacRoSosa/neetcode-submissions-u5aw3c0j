class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        ans = []
        n = len(nums)
        for num in nums:
            counter[num] += 1
            if counter[num] > n/3 and num not in ans:
                ans.append(num)
        return ans
