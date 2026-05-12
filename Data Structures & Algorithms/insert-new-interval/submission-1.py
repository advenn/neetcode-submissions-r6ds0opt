from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        # print(intervals)
        answer = [intervals[0]]
        # i = 0
        for s, e in intervals[1:]:
            if e <= answer[-1][1]:
                continue
            if s <= answer[-1][1]:
                answer[-1][1] = e
            else:
                answer.append([s, e])

        return answer