class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for i in range(len(nums)):
            one, two = max(one, two + nums[i]), one
        
        return one