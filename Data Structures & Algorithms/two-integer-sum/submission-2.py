class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prMap:
                return [prMap[diff], i]
            prMap[n] = i
