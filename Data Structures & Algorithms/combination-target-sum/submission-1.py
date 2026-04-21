class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def backtrack(current, start):
            match (s:= sum(current)):
                case _ if s == target:
                    answer.append(current[:])
                    return
                case _ if s > target:
                    return
                
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(current, i)
                current.pop()
        backtrack([], 0)
        return answer
