class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in idxMap:
                return [idxMap[diff], i]
            idxMap[n] = i
