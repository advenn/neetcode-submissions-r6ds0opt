class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        # seen = set()
        def backtrack(start, current):
            # Assuming 'current' and 'target' are defined
            match sum(current):
                case s if s == target:
                    answer.append(current[:])
                    return
                case s if s > target:
                    return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current)
                current.pop()
        backtrack(0, [])
        return answer

