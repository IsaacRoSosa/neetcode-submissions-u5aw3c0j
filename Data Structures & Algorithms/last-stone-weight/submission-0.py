import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Reverse for max heap
        stones = [-rock for rock in stones]
        heapq.heapify(stones)
        #Run simulation while we have more than stones
        while len(stones) >= 2:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            #both are desroyed continue cicle
            if x == y:
                pass
            elif x < y:
                heapq.heappush(stones, -(y - x))
            else:
                heapq.heappush(stones, -(x - y))

        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
