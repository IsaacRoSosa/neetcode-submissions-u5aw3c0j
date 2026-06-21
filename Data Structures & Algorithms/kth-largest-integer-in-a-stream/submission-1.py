import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.size = k

    def add(self, val: int) -> int:
        heap = self.heap
        heapq.heappush(heap, val)

        while len(heap) > self.size:
            heapq.heappop(heap)
        return heap[0]


        
