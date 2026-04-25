class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        
        maxmax = nums[0]
        lastmax = nums[0]
        lastmin = nums[0]

        for num in nums[1:]:
            curmax = max(num, lastmax * num, lastmin * num)
            lastmin = min(num, lastmax * num, lastmin * num)
            maxmax = max(lastmax, curmax, maxmax)
            lastmax = curmax
        return maxmax