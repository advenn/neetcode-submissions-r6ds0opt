class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -float("inf")
        so_far = -float("inf")
        for i in nums:
            so_far = max(so_far + i,i )
            best = max(best, so_far)
        return best