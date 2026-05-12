"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)

        last = intervals[0]

        for interv in intervals[1:]:
            if last.end > interv.start:
                return False
            else:
                last = interv
        return True