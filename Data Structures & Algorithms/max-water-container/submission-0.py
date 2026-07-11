class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input: List [] of int heights
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            width = right - left
            if heights[left] <= heights [right]:
                curArea = heights[left] * width
                if curArea > maxArea:
                    maxArea = curArea
                left += 1
            else: 
                curArea = heights[right] * width
                right -= 1
            
            maxArea = max(maxArea, curArea)

        return maxArea
        # Output: int max area between two highest points