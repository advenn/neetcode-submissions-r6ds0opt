class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dest, weight in times:
            graph[src].append((weight, dest))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            weight, src = heapq.heappop(heap)
            if weight > dist[src]:
                continue
            
            for cost, dest in graph[src]:
                new_cost = cost + weight
                if new_cost < dist[dest]:
                    dist[dest] = new_cost
                    heapq.heappush(heap, (new_cost, dest))
        
        m = max(dist[1:])
        return -1 if m == float("inf") else m