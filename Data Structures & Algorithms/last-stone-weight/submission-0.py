class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, (-stone, stone))
        
        while len(heap) >1:
            l1, l2 = heapq.heappop(heap), heapq.heappop(heap)
            if l1[0] == l2[0]:
                continue
            else:
                left =  abs(l2[1]-l1[1])
                heapq.heappush(heap,  (-left, left))
        return 0 if not heap else heap[0][1]
