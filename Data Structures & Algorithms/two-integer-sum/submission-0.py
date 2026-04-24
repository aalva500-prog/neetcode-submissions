class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):            
            if (target - num) in seen:
                return sorted([index, seen[target - num]])
            seen[num] = index
