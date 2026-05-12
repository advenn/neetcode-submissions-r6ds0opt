class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]

        for s,e in intervals[1:]:
            # if e <= answer[-1][1]:
            #     continue
            if s <= answer[-1][1]:
                answer[-1][1] = max(e, answer[-1][1])
            else:
                answer.append([s,e])
        return answer