class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        maxHeap = []
        #r is index
        for r, num in enumerate(nums):
            heapq.heappush(maxHeap, (-num,r))
            #Skip until we build the initial window 
            if r < k-1: continue
            #l = r-k+1
            #while our max element is not inside the current window, pop until we have a valid element
            while maxHeap[0][1] < (r-k+1):
                heapq.heappop(maxHeap)

            ans.append(-maxHeap[0][0])
        return ans