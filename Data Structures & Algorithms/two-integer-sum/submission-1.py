class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_id = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in pair_id:
                return [pair_id[complement], i]
            pair_id [num] = i
