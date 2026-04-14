class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums):
            seen[num] = index
        for index, num in enumerate(nums):
            # seen[num] = index
            complementary = target - num
            if complementary in seen and seen[complementary] != index:
                return [index, seen[complementary]]
        return []


        