class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}

        for i in range(len(nums)):
            if target - nums[i] in result_dict:
                return [result_dict.get(target - nums[i]), i]
            result_dict[nums[i]] = i
                