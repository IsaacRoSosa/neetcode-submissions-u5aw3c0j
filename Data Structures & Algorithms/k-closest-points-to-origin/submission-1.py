import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x,y = point
            distance = math.sqrt((x*x) + (y*y))
            heap.append((distance, [x,y]))
        ans = []
        heapq.heapify(heap)
        
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans


            

        