class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        answer = [False] * n
        answer[n - 1] = True
        # print(nums)
        for i in range(n - 2, -1, -1):
            # print(i, nums[i])
            for j in range(i, i + nums[i] + 1):
                # print(j)
                if j < n and answer[j]:
                    answer[i] = True

        return answer[0]
