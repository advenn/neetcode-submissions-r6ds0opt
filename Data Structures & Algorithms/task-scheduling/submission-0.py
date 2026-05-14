class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = defaultdict(int)
        for task in tasks:
            hashmap[task] += 1
        heap = [-v for v in hashmap.values()]
        heapq.heapify(heap)
        cooldown = deque()
        time = 0
        while heap or cooldown:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    cooldown.append((count, time + n))
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
        return time
