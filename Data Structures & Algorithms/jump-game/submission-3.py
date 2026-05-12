class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        answer = [False] * n
        answer[n - 1] = True
        for i in range(n - 2, -1, -1):
            for j in range(i, i + nums[i] + 1):
                if j < n and answer[j]:
                    answer[i] = True

        return answer[0]
