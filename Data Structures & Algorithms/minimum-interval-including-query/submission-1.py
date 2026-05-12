class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        original_queries = defaultdict(list)

        for i, q in enumerate(queries):
            original_queries[q].append(i)
        queries.sort()
        i = 0
        answer = [-1] * len(queries)
        heap = []
        for q in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r-l+1, r))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                for p in original_queries[q]:
                    answer[p] = heap[0][0]
        return answer