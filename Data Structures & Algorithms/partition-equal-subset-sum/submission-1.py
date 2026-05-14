class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        dp = {0}
        for num in nums:
            dp = {s + num for s in dp} | dp
        return target in dp