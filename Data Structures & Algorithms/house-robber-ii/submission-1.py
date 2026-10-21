class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        

        def helper(nums):
            one, two = 0, 0

            for n in nums:
                one, two = max(one, two + n), one
            
            return one
        

        return max(helper(nums[1:]), helper(nums[:-1]))


