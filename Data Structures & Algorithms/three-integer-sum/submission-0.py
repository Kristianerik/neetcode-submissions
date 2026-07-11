class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Input: array nums[-1,0,1,2,-1,-4]
        nums.sort()
        output = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left <right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current < 0:
                    left += 1
                else:
                    right -= 1

        return output 
        #output: list[[], []] where [] contains int + int + int == 0 