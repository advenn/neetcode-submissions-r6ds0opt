class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, price in flights:
            graph[s].append((d, price))
        heap = [(0, 0, src)]
        visited = {}

        while heap:
            price, stops, node = heapq.heappop(heap)
            if node == dst:
                return (price)
            if stops > k :
                continue
            if node in visited and visited[node] <=stops:
                continue
            visited[node] = stops
            for dest, cost in graph[node]:
                heapq.heappush(heap, (price + cost, stops + 1, dest))
        return -1
