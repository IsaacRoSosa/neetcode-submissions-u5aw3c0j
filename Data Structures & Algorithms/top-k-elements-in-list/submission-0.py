class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        sorted_keys = sorted(counter, key=counter.get, reverse=True)

        return sorted_keys[:k]
