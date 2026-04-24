class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:            
            for i, value in enumerate(left):
                if nums[i] == target:
                    return i
        else:            
            for j, value in enumerate(right, mid):
                if nums[j] == target:
                    return j

        return -1
        