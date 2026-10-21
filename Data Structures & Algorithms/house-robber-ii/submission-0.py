class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one, two = 0, 0
        
        for i in range(len(nums) - 1):
            one, two = max(one, two + nums[i]), one
        
        maxOne = one
        one, two = 0, 0

        for i in range(1, len(nums)):
            one, two = max(one, two + nums[i]), one
        
        maxTwo = one

        return max(maxOne, maxTwo)


