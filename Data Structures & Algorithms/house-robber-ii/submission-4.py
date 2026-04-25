class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def simple_rob(numbers):
            prev1, prev2 = 0,0
            for i in range( len(numbers)):
                best = max(prev2, prev1 + numbers[i])
                prev1=prev2
                prev2 = best            
            return prev2
        
        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))