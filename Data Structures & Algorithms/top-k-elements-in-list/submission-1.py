class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        i = 0

        for element, count in counter.most_common():
            ans.append(element)
            i+=1
            if i==k:
                return ans 
       



        
        