"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []

        for i in intervals:
            print(heap)
            if heap and i.start >= heap[0]:
                heapq.heapreplace(heap, i.end)

            else:
                heapq.heappush(heap, i.end)

        return len(heap)
