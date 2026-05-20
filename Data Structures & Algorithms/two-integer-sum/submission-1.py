class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        result = []

        for i in range(len(nums)):
            if target - nums[i] not in result_dict:
                result_dict[nums[i]] = i
            else:
                return [result_dict.get(target - nums[i]), i]
                