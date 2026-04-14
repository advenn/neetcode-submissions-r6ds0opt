class Solution:
    # do two sum, find pairs with target
    def twoSum(self, nums, target) -> list[list[int]]:
        twoSumResps = []
        l, r = 0, len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                twoSumResps.append([nums[l], nums[r]])
                while l<r and nums[l] == nums[l+1]: l += 1
                while l<r and nums[r] == nums[r-1]: r -= 1
                l += 1
                r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
        return twoSumResps


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # on three sum, find 
        if len(nums) < 3:
            return []

        nums.sort() 
        resp = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            right_pairs = self.twoSum(nums[i+1:], 0 - nums[i])
            for r in right_pairs:
                resp.append([r[0], r[1], nums[i]])
        return resp