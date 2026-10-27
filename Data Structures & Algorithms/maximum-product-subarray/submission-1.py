class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = minProd = result = nums[0]

        for i in range(1, len(nums)):
            temp = maxProd
            maxProd = max(nums[i], maxProd * nums[i], minProd * nums[i])
            minProd = min(nums[i], temp * nums[i], minProd * nums[i])
            result = max(result, maxProd)
        
        return result