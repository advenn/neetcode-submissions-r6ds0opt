class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(goal - 1, -1, -1):
            if goal <= i + nums[i]:
                goal = i
        return goal == 0
