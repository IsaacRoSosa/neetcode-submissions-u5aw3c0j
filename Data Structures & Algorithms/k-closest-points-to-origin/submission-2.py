import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            x,y = point
            distance = -((x*x) + (y*y))
            heapq.heappush(maxHeap,(distance,x,y))

            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        #return array with coordinates from inside maxheap
        return [[x, y] for _, x, y in maxHeap]


        
            

        