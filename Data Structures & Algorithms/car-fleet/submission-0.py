class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = sorted(zip(position, speed), reverse=True)
        get_time = lambda x:(target - x[0]) / x[1] 
        reach_times = [get_time(x) for x in positions]

        stack = []
        for rt in reach_times:
            if not stack:
                stack.append(rt)
                continue
            if rt > stack[-1]:
                stack.append(rt)
        return len(stack)